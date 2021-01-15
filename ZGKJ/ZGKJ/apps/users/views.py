import decimal
import logging
import random
import string
import time
import hashlib
import emoji as emoji
from weixin import WXAPPAPI
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from verification.views import Auth
from ZGKJ.settings.dev import APP_ID, APP_SECRET
from goods.models import User, SPU, Extract, USerDetailRank, Merchant, Collect, GoodsStyle
from django.core.paginator import Paginator
from django.http import HttpResponse


logger = logging.getLogger('django')

api = WXAPPAPI(appid=APP_ID,
               app_secret=APP_SECRET)


# Create your views here.
# 微信登录授权，并储存数据库tb_user,返回user.id
class WXLoginView(APIView):
    @staticmethod
    def randomStr():
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))
    @staticmethod
    def zgvip_code():
        return str(random.randint(100,999)).join(str(random.randint(100, 999)))

    def post(self, request):
        try:
            code = request.POST['code']

        except:
            logger.error('获取参数失败')
            return Response({'error_message': '获取参数失败'}, status=400)
        else:
            # 获取到code 去 交换会话密钥的代码
            session_info = api.exchange_code_for_session_key(code=code)
            # print(session_info)
            # 保存用户信息到数据库
            nickName = emoji.demojize(request.POST['nickName'])
            openId = session_info['openid']
            gender = request.POST['gender']
            language = request.POST['language']
            city = request.POST['city']
            ZGVIP_code = self.zgvip_code()
            province = request.POST['province']
            country = request.POST['country']
            avatarUrl = request.POST['avatarUrl']
            # 为了分销加邀请人信息(上级邀请人)
            invite_user_id=request.POST["invite_user_id"]
            invite_nickname=request.POST["invite_nickname"]
            logger.info('{0} - {1} - 解析成功'.format(nickName, openId))

            try:
                user = User.objects.get(openId=openId)
                print(user,'openid 获取')
            except Exception as e:
                # print(e)
                logger.info('{0} - {1} - 为新用户'.format(nickName, openId))
                # 查不到
                G = User( openId=openId, gender=gender, nickName=nickName,
                         language=language, wx_city=city, wx_province=province, ZGVIP_code=ZGVIP_code,  wx_country=country,
                         avatarUrl=avatarUrl, invite_nickname=invite_nickname, invite_user_id=invite_user_id, raise_base=0,
                         balance=0.00, onroad=0.00, invite_count=0, invitationCode='null', default_area=0)
                G.save()
                user = User.objects.get(openId=openId)
                user_id = user.id
                invitationCode = str(user_id) + self.randomStr()
                user.invitationCode = invitationCode
                user.save()
                # 通过上级邀请人去查 看是否还存在上上级邀请人
                try:
                    type_id = USerDetailRank.objects.get ( type_id=invite_user_id )
                except:
                    type_id = None
                if type_id:  # 如果存在
                    pass
                    # 找到 三级 入库
                    top_id = type_id.pid
                    userRank = USerDetailRank(top_id=top_id, pid=invite_user_id, type_id=user_id, top_code='', pid_code='')
                    userRank.save()
                else:
                    top_id = 0
                    pid = invite_user_id
                    userRank = USerDetailRank ( top_id=top_id, pid=pid, type_id=user_id, top_code='', pid_code='' )
                    userRank.save ()
                logger.info('{0} - {1} - 插入阶梯数据库成功'.format(nickName, openId))

            else:
                # 查到
                user.openId = openId
                user.gender = gender
                user.nickName = nickName
                user.language = language
                user.wx_city = city
                user.wx_province = province
                user. wx_country = country
                user.avatarUrl = avatarUrl
                user.ZGVIP_code = user.ZGVIP_code
                user.raise_base = user.raise_base
                user.invite_nickname = user.invite_nickname
                user.invite_user_id = user.invite_user_id
                user.balance = user.balance
                user.onroad = user.onroad
                user.invite_count = user.invite_count
                user.invitationCode = 'asdd'
                user.default_area = 0
                user.star_id = 48
                user.save ()
                users = User.objects.get ( openId=openId )
                user_id = users.id
                invitationCode = str ( user_id ) + self.randomStr ()
                users.invitationCode = invitationCode
                users.save ()
                # user.nickName = nickName
                # user.openId = openId
                # user.gender = gender
                # user.language = language
                # user.wx_city = city
                # user.wx_country = country
                # user.wx_province = province
                # user.avatarUrl = avatarUrl

                logger.info('{0} - {1} - 老用户修改基本信息成功'.format(nickName, openId))

            jwt_token = Auth.encode_auth_token(user.id, str(int(time.time())))
            logger.info(jwt_token)
            # return Response({"code":user.invitationCode,"token": jwt_token,"nickname":user.nickName, "user_id": user.id,"invite_user_id":user.invite_user_id,"invite_nickname":user.invite_nickname,"balance":user.balance})
            return Response(
                {"code": user.invitationCode, "token": jwt_token, "nickname": user.nickName, "user_id": user.id,
                 "invite_user_id": user.invite_user_id, "invite_nickname": user.invite_nickname,
                 "balance": user.balance, "onroad": user.onroad,'ZGVIP_code':user.ZGVIP_code})


# 用户中心
class UserCenter(APIView):
    def get(self, request):
        user = User.objects.get(id=request.wx_user.id)
        withdraw_cash = Extract.objects.filter(user_id=user.id).aggregate(withdraw_cash=Sum('extract_money'))['withdraw_cash']
        # print(withdraw_cash,'萨达撒打算多')
        #提现到账金额
        withdraw_cash = withdraw_cash if withdraw_cash is not None else 0.00
        # print(user.balance)
        receive_cash = decimal.Decimal(withdraw_cash) + decimal.Decimal(user.balance)
        return Response({
            "nickname": user.nickName,
            "balance": user.balance,
            "onroad": user.onroad,
            "user_id": user.id,
            "invite_user_id": user.invite_user_id,
            "invite_nickname": user.invite_nickname,
            "withdraw_cash": withdraw_cash,
            "receive_cash": receive_cash
        })


# 用户收藏
class UserStarList(APIView):
    '''
    User collection list data acquisition,
    '''
    def get(self, request):
        mes = dict()
        user_id = request.wx_user.id
        # print(user_id)
        # print(type(user_id))
        current_pagnum = request.GET.get ( 'p', 1 )
        # 查询 id 下的数据
        collect = Collect.objects.filter ( user_id=user_id  ).all ()
        paginator = Paginator ( collect, 2 )  # 每页显示几个
        posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
        num_pages = paginator.num_pages  # 总页数

        collectList = list()
        for i in collect:
            goodsDict = dict()
            goodsDict['goods_name'] = i.spu.name # 商品名称
            goodsDict['spu_code'] = i.spu.spu_code # 商品编码
            goodsDict['subTitle'] = i.spu.subTitle # 详情简介
            goods = GoodsStyle.objects.filter ( spu_code_id=i.spu.spu_code ).all()
            goodsStyleList = list()
            for j in goods:
                styledict = dict()
                styledict['price'] = j.price # 商品价格
                styledict['qiniu_image_url'] = j.qiniu_image_url # 商品tu
                styledict['default_image_url'] = j.default_image_url # 商品tu
                goodsStyleList.append(styledict)
            goodsDict['goodsStyleList'] = goodsStyleList
            collectList.append(goodsDict)
        mes['collectList'] = collectList
        mes['code'] = status.HTTP_200_OK
        mes['message'] = 'The query is succssful'
        return Response(mes)

    def post(self, request):
        data = request.data
        mes = dict()
        try:
            spu_code = data['spu_code']
            user_id = request.wx_user.id
            try: #查询 收藏表是否存在当前商品收藏
                collect = Collect.objects.get ( user_id=user_id, spu__spu_code=spu_code )
            except:# 没有则添加收藏
                collect = Collect ()
                collect.user_id = user_id
                collect.spu_id = SPU.objects.get ( spu_code=spu_code ).id
                collect.save ()
                mes[ 'code' ] = status.HTTP_200_OK
                mes[ 'message' ] = 'Collection of success'
            else: #有则取消
                collect.delete ()
                mes[ 'code' ] = status.HTTP_200_OK
                mes[ 'message' ] = 'Cancel the collection successfully'
        except: #获取参数不正确
            mes[ 'code' ] = status.HTTP_400_BAD_REQUEST
            mes[ 'message' ] = 'Request error '
        return Response(mes)


# 特邀代理商填写信息接口
class SpecialAgent(APIView):
    def post( self, request):
        mes = dict()
        data = request.data
        wx_code = data['wx_code']
        wx_name = request.wx_user.nickName
        wx_id = request.wx_user.ZGVIP_code
        if all([wx_code, wx_name, wx_id]):
            try:
                wx = Merchant.objects.get(wx_code=wx_code)
            except:
                wx = None
            if wx != None:
                wx.wx_id = wx_id
                wx.wx_name = wx_name
                wx.save()
                mes['code'] = status.HTTP_200_OK
                mes['message'] = 'Successfully join the invited agent'
            else:
                mes[ 'code' ] = status.HTTP_417_EXPECTATION_FAILED
                mes[ 'message' ] = 'The invitation code you entered does not exist'
        else:
            mes[ 'code' ] = status.HTTP_400_BAD_REQUEST
            mes[ 'message' ] = 'Error request parameter missing'

        return Response(mes)



class WeiXinToken(APIView):
    def get (self, request ):
        print('token 开始')
        signature = request.GET.get ( 'signature' )
        timestamp = request.GET.get ( 'timestamp' )
        nonce = request.GET.get ( 'nonce' )
        echostr = request.GET.get ( 'echostr' )
        token = "zugoutoken123456789"
        tmpArr = [ token, timestamp, nonce ]
        tmpArr.sort ()
        string = ''.join ( tmpArr ).encode ( 'utf-8' )
        string = hashlib.sha1 ( string ).hexdigest ()
        if string == signature:
            print('--------------------------------')
            print(string)
            print(signature)
            return HttpResponse ( echostr )
        else:
            return HttpResponse ( "false" )
