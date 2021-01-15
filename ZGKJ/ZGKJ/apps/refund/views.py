import datetime
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from goods.models import OrderInfo,SalesReturn,RefundOrder

now_time = datetime.datetime.now ()


class Refund ( APIView ):
    """退款"""

    @staticmethod
    def born_out_trade_no ():
        out_trade_no = str ( "TK" ) + str ( now_time.year ) + str ( now_time.month ) + str ( now_time.day ) + str (
            random.randrange ( 100000, 999999 ) ) + str ( random.randrange ( 1000, 9999 ) )
        return out_trade_no

    def post ( self, request ):
        """提交退货订单"""
        out_refund_no = self.born_out_trade_no ()
        order_sn = request.POST.get ( "order_sn" )
        refund_amount = request.POST.get ( "refund_amount" )
        print(refund_amount,"退款金额")
        re_type = request.POST.get ( "re_type" )
        reason = request.POST.get ( "refund_reason" )
        # 验证订单
        try:
            order = OrderInfo.objects.get ( order_sn=order_sn )
        except:
            return Response ( {"code": 400, "msg": "没有该订单"} )
        # 验证订单金额
        print(order.actual_payment,"实际支付")
        print(1 if float(refund_amount) <= float(order.actual_payment) else 2 )
        if  float(refund_amount) > float(order.actual_payment):
            return Response ( {"code": 400, "msg": "退款金额不能大于订单金额"} )
        # elif float(refund_amount) == float(order.actual_payment):
        else:
            # 新增退款订单
            RefundOrder ( refund_reason=reason, re_type=re_type, user_id=order.user_id, order_sn=order_sn,
                          out_refund_no=out_refund_no,
                          order_amount=order.actual_payment, refund_amount=refund_amount, is_refund=False, status=1,goods_name=order.goods_name, user_info=order.user_info, goodsNumber=order.goodsNumber, goods_spu=order.goods_spu ).save ()
            order.status = 7
            order.save()

        return Response ( {'code': 200, 'mes': '退款订单已提交,等到商家确认'} )

class RefundDetail(APIView):
    def get( self, request):
        mes = dict ()
        order_sn = request.GET.get('order_sn', '')
        try:
            i = RefundOrder.objects.get(order_sn=order_sn)
        except:
            mes[ 'code' ] = 400
            mes[ 'message' ] = '系统繁忙'
            mes[ 'data' ] = []
            return Response ( mes )
        order = OrderInfo.objects.get(order_sn=i.order_sn)
        datalist = list()
        data = dict()
        orderlist = dict()
        data[ 'id' ] = i.id
        data[ 'create_time' ] = i.create_time.strftime ( '%Y-%m-%d %Z %H:%M:%S' )
        data[ 'user_id' ] = i.user_id
        data[ 'out_refund_no' ] = i.out_refund_no
        data[ 'order_sn' ] = i.order_sn
        data[ 'order_amount' ] = i.order_amount
        data[ 'refund_amount' ] = i.refund_amount
        data[ 'is_refund' ] = i.is_refund
        data[ 'status' ] = i.status
        data[ 'is_refund' ] = i.is_refund
        data[ 'not_pass_reason' ] = i.not_pass_reason
        data[ 'refund_reason' ] = i.refund_reason
        data[ 're_type' ] = i.re_type
        data[ 'logistics_no' ] = i.logistics_no
        try:
            sales = SalesReturn.objects.get ( id=int ( i.logistics_company ) )
            data[ 'name' ] = sales.name
            data[ 'phone' ] = sales.phone
            data[ 'address' ] = sales.address
            data[ 'detail' ] = sales.detail
        except:
            data[ 'name' ] = None
            data[ 'phone' ] = None
            data[ 'address' ] = None
            data[ 'detail' ] = None
        orderlist['goods_name'] = order.goods_name
        orderlist['total_count'] = order.total_count
        orderlist['goods_color'] = order.goods_color
        orderlist['price'] = order.price
        orderlist['total_amount'] = order.total_amount
        orderlist['size'] = order.size
        orderlist['freight'] = order.freight
        orderlist['image'] = order.image
        orderlist['actual_payment'] = order.actual_payment
        data['orderdetail'] = orderlist
        datalist.append(data)
        mes['code'] =200
        mes['message'] = '查询成功'
        mes['data'] = datalist
        return Response(mes)


# 用户取消退款单
class OffOrder(APIView):
    def put( self, request):
        mes = dict()
        try:
            out_refund_no = request.data['out_refund_no']
            refund = RefundOrder.objects.get(out_refund_no=out_refund_no)
            order = OrderInfo.objects.get ( order_sn=refund.order_sn )
            if refund.re_type == 1:
                order.status = 4
                order.save()
                refund.delete()
            else:
                order.status =  2
                order.save()
                refund.delete ()
            mes[ 'code' ] = 200
            mes[ 'message' ] = '操作成功'
        except:
            mes[ 'code' ] = 500
            mes[ 'message' ] = '系统繁忙'
        return Response(mes)


class RefundWuLiu(APIView):
    '''
    :param company 物流公司
    :param logistics_no 物流单号
    :param out_refund_no 退款单号
    '''
    ''' Users add returned goods and fill in the logistics information '''
    def put( self, request):
        data = request.data
        company = data['company']
        logistics_no = data['logistics_no']
        out_refund_no = data['out_refund_no']
        try:
            refund = RefundOrder.objects.get(out_refund_no=out_refund_no)
        except:
            mes = {'code':400, 'message':'没有该退款单信息'}
        else:
            refund.logistics_no = "物流公司: " + company + '单号:  ' + logistics_no
            refund.status = 3
            refund.save()
            mes = {'code':200, 'message':'添加物流信息成功'}
        return Response(mes)