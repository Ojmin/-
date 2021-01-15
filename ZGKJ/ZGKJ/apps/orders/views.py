import datetime
import logging
import random
import redis
import decimal
import requests
from django.core.paginator import Paginator
from redis import StrictRedis
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ZGKJ.utils.redis_pool import POOL
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.models import GoodsStock, OrderInfo, SPU, UserAcceptGoodAreaModel, GoodsStyle,GoodsNumbers, User
from orders.utils import enquiry_logistics
from orders.serializers import *
logger = logging.getLogger('django')

now_time = datetime.datetime.now()


class OrderView(APIView):
    """订单"""

    @staticmethod
    def born_out_trade_no():
        out_trade_no = str(now_time.year) + str(now_time.month) + str(now_time.day) + str(
            random.randrange(100000, 999999)) + str(random.randrange(1000, 9999))
        return out_trade_no

    def get(self, request):
        mes = dict ()
        user_id = request.wx_user.id
        status = request.GET.get('status', None)
        if  status != '0':
            alist = []
            for i in status.split(','):
                if i == '':
                   continue
                alist.append(int(i))
            try:
                all_order = OrderInfo.objects.filter(user_id=user_id, is_deleted=False, status__in=alist).order_by('-payment_time')
            except:
                mes[ 'code' ] = 400
                mes[ 'message' ] = 'select error'
                mes[ 'order_list' ] = []
            else:
                current_pagnum = request.GET.get ( 'p', 1 )
                paginator = Paginator ( all_order, 10 )  # 每页显示几个
                posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
                num_pages = paginator.num_pages  # 总页数
                orderList = list ()
                for order in posts:
                    data = dict()
                    data['out_trade_no'] = order.order_sn
                    data['goodsNumber'] = order.goodsNumber
                    data['subTitle'] = SPU.objects.get(spu_code=order.goods_spu).subTitle
                    data['price'] = order.price
                    data['size'] = order.size
                    data['address'] = {'province':order.address.province ,
                                       'city':order.address.city ,
                                       'district':order.address.district,
                                       'place': order.address.place,
                                       'mobile':order.address.mobile,
                                       'AcceptPerson':order.address.AcceptPerson
                                       }
                    data['total_count'] = order.total_count
                    data['total_amount'] = order.total_amount
                    data['freight'] = order.freight
                    data['status'] = order.status
                    data['goods_color'] = order.goods_color
                    data['wuliu_info'] = order.wuliu_info
                    data['create_time'] = order.payment_time
                    data['image'] = order.image
                    data['title'] = order.goods_name
                    orderList.append(data)
                mes[ 'code' ] = 200
                mes[ 'message' ] = 'select success'
                mes[ 'order_list' ] = orderList
                mes['tpage'] = num_pages
        else:
            try:
                all_order = OrderInfo.objects.filter(user_id=user_id, is_deleted=False).order_by('-payment_time')
            except:
                mes[ 'code' ] = 400
                mes[ 'message' ] = 'select error'
                mes[ 'order_list' ] = []
            else:
                current_pagnum = request.GET.get ( 'p', 1 )
                paginator = Paginator ( all_order, 10 )  # 每页显示几个
                posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
                num_pages = paginator.num_pages  # 总页数
                orderList = list ()
                for order in posts:
                    data = dict()
                    data['out_trade_no'] = order.order_sn
                    data['goodsNumber'] = order.goodsNumber
                    data['subTitle'] = SPU.objects.get(spu_code=order.goods_spu).subTitle
                    data['price'] = order.price
                    data['size'] = order.size
                    data['address'] = {'province':order.address.province ,
                                       'city':order.address.city ,
                                       'district':order.address.district,
                                       'place': order.address.place,
                                       'mobile':order.address.mobile,
                                       'AcceptPerson':order.address.AcceptPerson
                                       }
                    data['total_count'] = order.total_count
                    data['total_amount'] = order.total_amount
                    data['freight'] = order.freight
                    data['status'] = order.status
                    data['goods_color'] = order.goods_color
                    data['wuliu_info'] = order.wuliu_info
                    data['create_time'] = order.payment_time
                    data['image'] = order.image
                    data['title'] = order.goods_name
                    orderList.append(data)
                mes[ 'code' ] = 200
                mes[ 'message' ] = 'select success'
                mes[ 'order_list' ] = orderList
                mes['tpage'] = num_pages
        return Response(mes)

    def post(self, request):
        size = request.POST['size']
        goodsNumber = request.POST['goodsNumber']
        count = request.POST['count']
        # 查库存
        goods_size = GoodsNumbers.objects.get(goodsNumber=goodsNumber, goods_size=size)
        # logger.info(goods_size)
        stock = goods_size.goods_count
        if int(count) > int(stock):
            return Response({"message": '库存不足'})
        else:
            # 更新库存
            stock -= int(count)
            goods_size.goods_count = stock
            goods_size.save()
            # user_id = request.POST['user_id']
            # 传地址的id
            goods_color = request.POST[ 'goods_color' ]
            goods_spu = request.POST[ 'goods_spu' ]
            user_nickname = request.POST.get ( "user_nickname" )
            invite_user_id = request.POST.get ( "invite_user_id" )
            invite_nickname = request.POST.get ( "invite_nickname" )
            print ( invite_nickname )
            area_id = request.POST['area_id']
            price = request.POST['price']
            total_amount = request.POST['total_amount']
            freight = request.POST['freight']
            title = request.POST['title']
            image = request.POST['image']
            # subTitle = request.POST['subTitle']
            out_trade_no = self.born_out_trade_no()
            user_id = request.wx_user.id
            address = UserAcceptGoodAreaModel.objects.get(id=area_id)
            # 保存订单信息
            OrderInfo(user_id=user_id,
                      order_sn=out_trade_no,
                      actual_payment=decimal.Decimal(total_amount)+decimal.Decimal(freight),
                      address=address,
                      total_amount=total_amount,
                      price=price,
                      goods_color=goods_color,
                      total_count=count,
                      freight=freight,
                      goodsNumber=goodsNumber,
                      image=image,
                      goods_spu=goods_spu,
                      is_deleted=False,
                      goods_name=title,
                      user_info='收货人: ' + address.AcceptPerson + " 电话: " + address.mobile + "  地址: " + address.province + \
                                address.city + address.district + address.place,
                      wuliu_info = '',
                      size=size,
                      status=1,
                      invite_nickname=invite_nickname,
                      user_nickname=user_nickname,
                      invite_user_id=invite_user_id,
                      ).save()
            # 建立reids连接
            conn = StrictRedis ( host='127.0.0.1', port=6379, decode_responses=True,db=10 )
            # 保存redis并返回给前端
            conn.set ( out_trade_no, user_id, ex=60 )
            return Response({'code': 1001, 'msg': '生成订单成功', 'out_trade_no': out_trade_no}, status=status.HTTP_200_OK)

    # 删除订单
    def delete(self, request):
        out_trade_no = request.data['out_trade_no']
        order = OrderInfo.objects.get(order_sn=out_trade_no)
        order.is_deleted = True
        order.save()
        return Response('删除订单{}成功'.format(out_trade_no), status=status.HTTP_200_OK)

    # 取消订单
    def put(self, request):
        out_trade_no = request.data['out_trade_no']
        reason = request.data['reason']
        # 要把库存加回来
        order = OrderInfo.objects.get(order_sn=out_trade_no)
        goodsNumber = order.goodsNumber
        size = order.size
        count = order.total_count
        goods_size = GoodsNumbers.objects.get(goodsNumber=goodsNumber, size=size)
        stock = goods_size.stock
        goods_size.stock = stock + int(count)
        goods_size.save()
        order.status = 6
        order.reason = reason
        order.save()
        return Response('取消订单{}成功'.format(out_trade_no), status=status.HTTP_200_OK)


# 订单详情
class OrderDetail(APIView):
    """订单详情"""

    def get(self, request):
        try:
            out_trade_no = request.GET['out_trade_no']
            orderDetail = OrderInfo.objects.get(order_sn=out_trade_no)
        except Exception as e:
            logger.info('没有 {} 的订单'.format(out_trade_no))
            return Response('没有{}订单号'.format(out_trade_no), status=status.HTTP_400_BAD_REQUEST)
        data = {}
        data['out_trade_no'] = orderDetail.order_sn
        data['subTitle'] = SPU.objects.get(spu_code=orderDetail.goods_spu).subTitle
        data['goodsNumber'] = orderDetail.goodsNumber
        data['create_time'] = orderDetail.create_time.strftime ( '%Y-%m-%d %Z %H:%M:%S' ) 
        data['size'] = orderDetail.size
        logistics_no = orderDetail.wuliu_info.split(',')[-1]
        data['logistics_no'] = logistics_no
        data['goods_color'] = orderDetail.goods_color
        data['total_count'] = orderDetail.total_count
        data['total_amount'] = orderDetail.total_amount
        data['freight'] = orderDetail.freight
        data['status'] = orderDetail.status
        data['payment_time'] = orderDetail.payment_time
        data['image'] = orderDetail.image
        data['spu_code'] = orderDetail.goods_spu
        data['price'] = orderDetail.price
        data['title'] = orderDetail.goods_name
        data['address'] = {
            'AcceptPerson': orderDetail.address.AcceptPerson,
            'province': orderDetail.address.province,
            'city': orderDetail.address.city,
            'district': orderDetail.address.district,
            'place': orderDetail.address.place,
            'mobile': orderDetail.address.mobile,
        }

        return Response(data, status=status.HTTP_200_OK)


class LogisticsView(APIView):
    """物流信息的获取"""

    def get(self, request):
        logistics_no = request.GET['logistics_no']
        company_no = request.GET['company_no']
        try:
            res = enquiry_logistics(logistics_no, company_no)
        except:
            res = {'msg': '没有查到该单号,请添加公司编号'}
        return Response(res, status=status.HTTP_200_OK)


# 首页
class Index(APIView):
    """首页"""

    def get(self, request):
        return render(request, 'index.html')
#
# class OrderStatusOne(APIView):
#     def get( self, request):
#         # OrderInfo.objects.filter(status=1,payment_time=# )
#         pass

@require_http_methods(["POST"])
@csrf_exempt
def notifications(request):
    if request.method == 'POST':
        APPID = 'wx45221ea345e0df25'
        APP_SECRET = '31c9da1a09c8b354d45510388a90fc03'
        payload = {
    'grant_type': 'client_credential',
    'appid': APPID,
    'secret': APP_SECRET
    }

        # req = requests.get('https://api.weixin.qq.com/cgi-bin/token?', params=payload, timeout=3, verify=False)
        # access_token = req.json().get('access_token')
        # print(access_token,'token ')
        conn = redis.Redis ( connection_pool=POOL )
        access_token = conn.get('access_token') 
        # print(access_token,'token')
        order_sn = request.POST.get('order_sn')
        
        # print(order_sn)
        order = OrderInfo.objects.get(order_sn=order_sn)
        template_id = 'aDVo4C9fjuED_o3gN8jXSuiA18KpCo9aY_HaRdMu3gk'
        push_data = {
            "thing01": {
                "value": order.order_sn
            },
            "thing02": {
                "value": order.goods_name
            },
            "amount01": {
                "value": order.total_amount
            },
            "thing03": {
                "value": order.payment_time.strftime ( '%Y-%m-%d %Z %H:%M:%S' )
            },
            "thing04": {
                "value": "商家已发货"
            },
        }

        if access_token:
            # 如果存在accesstoken
            user = User.objects.get(id=order.user_id)
            print(user.openId,'用户')
            payload = {
                'touser': user.openId, #这里为用户的openid
                'template_id': template_id, #模板id
                # 'form_id': req_data.get('form_id', ''), #表单id或者prepay_id
                'data': push_data #模板填充的数据
            }

            response = requests.post('https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=ACCESS_TOKEN={}'.format(access_token),
                          json=payload)

            #直接返回res结果
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'err': 'access_token missing'
            })


import time
class UserWithdrawcash(APIView):
    def put( self, request):
        id = request.wx_user.id
        try:
            ex = OrderInfo.objects.filter(user_id=id).all()
        except:
            return Response({'code':200,'mes':'无订单数据'})
        end_time = time.time ()
        mes = dict()
        for i in ex:
            # 转换成时间数组
            timeArray = i.payment_time.strftime ( '%Y-%m-%d %Z %H:%M:%S' )
            # print(timeArray,'asdasdasdas')

            # 转换成时间戳
            timestamp = time.mktime ( time.strptime ( timeArray, '%Y-%m-%d %H:%M:%S' ) )
            if end_time - timestamp >= 86400.00:
                if i.status == 6:
                    pass
                i.status = 6
                i.save()
                mes['code']=200
                mes['message'] = 'update successful'
            else:
                return Response ( {'code': 200, 'mes': '订单数据没有大于7天的'} )
        return Response(mes)


class RefundList(APIView):
    def put(self, request):
        mes = dict ()
        data = request.data
        out_refund_no = data['out_refund_no']
        print(out_refund_no)
        if  out_refund_no is not None:
            refund = RefundOrder.objects.get(out_refund_no=out_refund_no)
            refund.status = 1
            order = OrderInfo.objects.get(order_sn=refund.order_sn)
            order.status = 7
            refund.save()
            order.save()
            mes['code'] = 200
            mes['message'] = '重新发起订单成功'
        else:
            mes[ 'code' ] = 400
            mes[ 'message' ] = '重新发起订单失败'
        return Response(mes)