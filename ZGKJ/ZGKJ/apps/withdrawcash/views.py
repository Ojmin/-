import json
import decimal
import logging
import random
import time
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from weixin.pay import wxpay_notify_verify, WeixinEnterprisePay, WeixinPay
from django.db.models.aggregates import Sum
from ZGKJ.settings.dev import SIGN_KEY, APP_ID, APP_MCH_ID, APP_PARTNER_KEY
from goods.models import User, OrderInfo
from goods.models import Extract, Commission, Merchant

logger = logging.getLogger ( 'django' )


class WithdrawCash ( APIView ):
    # 增加提现订单表
    def post ( self, request ):

        user_id = request.POST.get ( "user_id" ,None)
        amount = float(request.POST.get ( "amount" ,None)) 
        exract_sn = self.gen_order_num ( "TX" )
        if user_id is not None and amount is not None:
            if amount < 0.3:
                return Response ( {"code": 400, "msg": "金额不得小于0.3"} )

            user = User.objects.get(id=user_id)

            if user.balance < amount:
                return Response ( {"code": 400, "msg": "用户余额不足"} )

            G = Extract ( user_id=user_id, extract_money=amount, exract_sn=exract_sn, wx_username=request.wx_user.nickName,
                          status=1 )
            G.save ()
            user.balance = user.balance - decimal.Decimal(amount)
            user.save ()
            logger.info ( "增加提现订单表{}金额{}".format ( exract_sn, amount ) )
            return Response ( {"code": 200, "msg": "更新订单表成功", "exract_sn": exract_sn} )
        else:
            return Response ( {"code": 400, "msg": "提交金额有误"} )

    @staticmethod
    def gen_order_num ( prefix ):
        s = str ( random.randrange ( 1000, 9999 ) )
        return prefix + str ( int ( round ( time.time () * 1000 ) ) ) + str ( s )

    # 查提现订单表
    def get ( self, request ):
        id = request.GET.get ( "id" )
        print ( id )
        user_id = request.GET.get ( "user_id" )
        page = request.GET.get ( "page" )
        data = {"page": 1}
        print ( id )
        if user_id != None:
            orders = Extract.objects.filter ( user_id=user_id ).all ().order_by ( '-exract_time' )
            paginator = Paginator ( orders, 20 )  # 每页显示几个
            posts = paginator.page ( number=int ( page ) )  # 这个num就是现实当前第几页
            num_pages = paginator.num_pages  # 总页数
            array = [ ]
            for order in posts:
                rows = {"id": order.id,
                        "exract_sn": order.exract_sn,
                        "user_id": order.user_id,
                        "amount": order.extract_money,
                        "status": order.status,
                        "create_time": order.exract_time.strftime ( '%Y-%m-%d %Z %H:%M:%S' )
                        }
                array.append ( rows )
            data[ "page" ] = num_pages
            data[ "rows" ] = array
            data[ 'code' ] = 200
            data[ 'message' ] = 'query is successful'
        else:
            data[ 'code' ] = 200
            data[ 'message' ] = 'query is successfuls'
            data[ "rows" ] = [ ]
        return Response ( data )


class BusinessPay ( APIView ):
    def post ( self, request ):
        js = json.loads ( request.body )
        user_id = js[ "user_id" ]
        exract_sn = js[ "exract_sn" ]
        print ( js )
        if not wxpay_notify_verify ( js, SIGN_KEY ):
            return Response ( {"code": 400, "msg": "签名错误"} )
        # 验证用户
        try:
            user = User.objects.get ( id=user_id )
        except:
            return Response ( {"code": 400, "msg": "没有该用户"} )
        # 验证订单
        try:
            order = Extract.objects.get ( exract_sn=exract_sn )
        except:
            return Response ( {"code": 400, "msg": "没有该订单"} )
        fee_cash = int ( float ( order.extract_money ) * 100 )
        # 微信支付
        ret = WeixinEnterprisePay ( appid=APP_ID,
                                    mch_id=APP_MCH_ID,
                                    notify_url="https://www.zugou.vip/payResult",
                                    partner_key=APP_PARTNER_KEY,
                                    mch_cert="/home/zgkjMall/ZGKJ/1552385571_20191205_cert/apiclient_cert.pem",
                                    mch_key="/home/zgkjMall/ZGKJ/1552385571_20191205_cert/apiclient_key.pem" ).transfers (
            exract_sn, user.openId, fee_cash,
            "邀请奖励", "47.100.90.244" )
        logger.info (ret)
        
        if ret[ "return_code" ] == "SUCCESS" and ret[ "result_code" ] == "SUCCESS":
            order.status = 2
            order.save ()
            logger.info (
                str ( user_id ) + "提现了" + str ( order.extract_money ) + "元,订单号:" + str ( exract_sn ) + "提现时间:" + str (
                    order.exract_time ) )
            return Response ( {"code": 200, "msg": "提现成功"} )
        else:
            logger.info('提现失败')
            return Response ( {"code": 400, "msg": "提现失败,请联系客服!"} )


# 邀请人收益列表(用户中心-->小足金)
class InvitationInfo ( APIView ):
    def get ( self, request ):
        user_id = request.GET.get ( "user_id" )
        page = request.GET.get ( "page" )
        try:
            # 作为二级收益人的数据
            all_info = Commission.objects.filter (
                Q ( up_wx_user_id=int ( user_id ) ) | Q ( up_up_wx_user_id=int ( user_id ) ) ).all ()
            print ( all_info )
        except Exception as e:
            print ( e )
            return Response ( {"code": 400, "msg": "没有该用户", 'rows': [ ]} )
        paginator = Paginator ( all_info, 20 )  # 每页显示几个
        posts = paginator.page ( number=int ( page ) )  # 这个num就是现实当前第几页
        num_pages = paginator.num_pages  # 总页数
        array = [ ]
        data = {}
        for invitation in posts:
            rows = dict ()
            if int ( user_id ) == invitation.up_wx_user_id:
                rows[ "id" ] = invitation.id
                rows[ "buyer_wx_name" ] = invitation.buyer_wx_name  # 微信买家名称
                rows[ "actual_payment" ] = invitation.actual_payment  # 实际价格
                rows[ "goods_name" ] = OrderInfo.objects.get ( order_sn=invitation.order_num ).goods_name  # 商品名称
                rows[ "gain_money" ] = invitation.up_gain_money  #
            else:
                rows[ "id" ] = invitation.id
                rows[ "buyer_wx_name" ] = invitation.buyer_wx_name  # 微信买家名称
                rows[ "actual_payment" ] = invitation.actual_payment  # 实际价格
                rows[ "goods_name" ] = OrderInfo.objects.get ( order_sn=invitation.order_num ).goods_name  # 商品名称
                rows[ "gain_money" ] = invitation.up_up_gain
            array.append ( rows )
        data[ "page" ] = num_pages
        data[ "rows" ] = array
        return Response ( data )


class UserInfoView ( APIView ):
    '''用户钱包'''

    def get ( self, request ):
        user_id = request.wx_user.id
        print(user_id,'用户iD')
        user = User.objects.get ( id=int ( user_id ) )
        extrace = Extract.objects.filter ( user_id=int ( user_id ) ).aggregate ( Sumnums=Sum ( 'extract_money' ) ).get (
            'Sumnums' ) or 0.00
        print ( extrace, '用户提现金额' )
        mes = dict ()
        if extrace != 0:
            mes[ 'nums' ] = extrace
            mes[ 'amount' ] = decimal.Decimal ( user.balance + extrace )
        else:
            mes[ 'nums' ] = extrace
            mes[ 'amount' ] = decimal.Decimal ( user.balance + 0 )
        try:
            merchant = Merchant.objects.get ( wx_id=user.ZGVIP_code )
        except:
            merchant = None
        if merchant:
            mes[ 'merchant' ] = 1
        else:
            mes[ 'merchant' ] = 0
        mes[ 'balance' ] = user.balance
        mes[ 'onroad' ] = user.onroad
        mes[ 'code' ] = 200
        mes[ 'message' ] = 'query is successful'
        return Response ( mes )

#
# if __name__ == '__main__':
#     print(WithdrawCash.gen_order_num("TX"))
