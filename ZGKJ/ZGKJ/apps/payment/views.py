import decimal
import json
import logging
import pickle
import random
import time
import string
import requests
import xmltodict
import hashlib
import xml.etree.ElementTree as et
import datetime
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ZGKJ.settings.dev import APP_ID, APP_MCH_ID, APP_PARTNER_KEY, SIGN_KEY
from goods.models import OrderInfo, User, Commission, USerDetailRank, Merchant, Ladder, RankSell, GoodsNumbers, SPU
from payment.constent import PERCENT
from weixin.pay import WXAppPay, wxpay_notify_verify

toOrderUrl = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
logger = logging.getLogger ( 'django' )

# 创建小程序对象
wxpay = WXAppPay ( appid=APP_ID,
                   mch_id=APP_MCH_ID,
                   notify_url="https://www.zugou.vip/payResult",
                   partner_key=APP_PARTNER_KEY )

now_time = datetime.datetime.now ()


class PayView ( APIView ):
    """支付"""

    # 预支付，统一下单
    def post ( self, request ):
        user = request.wx_user
        # print("user.pid: ",user.nickName)
        openId = user.openId
        total_amount = request.POST[ 'total_amount' ]
        subTitle = request.POST[ 'subTitle' ]
        out_trade_no = request.POST[ 'out_trade_no' ]
        logger.info("下单支付时的订单号:{} ".format(out_trade_no))
        # 统一下单
        # print("openid: ",openId)

        # print("appid: ", APP_ID)
        nonce_str = WXUtils.randomStr ()
        params = {
            'appid': APP_ID,
            'mch_id': APP_MCH_ID,
            'nonce_str': nonce_str,
            'profit_sharing':"Y",
            'body': subTitle,  # 商品描述，通过request对象获取，前段传过来
            "out_trade_no": out_trade_no,
            "total_fee": int ( float ( total_amount ) * 100 ),  # 单位分，金额
            "spbill_create_ip": "47.100.90.244",
            "notify_url": "https://www.zugou.vip/payResult",  # 支付成功的回馈地址
            "trade_type": "JSAPI",  # 交易类型 小程序定死jsapi
            "openid": openId
        }
        sign = WXUtils.wx_sign ( params )
        params[ 'sign' ] = sign
        xmlmsg = WXUtils.send_xml_request ( toOrderUrl, params )
        if xmlmsg[ 'xml' ][ 'return_code' ] == 'SUCCESS':
            # print(xmlmsg)
            try:
                prepay_id = xmlmsg[ 'xml' ][ 'prepay_id' ]
                logger.info("支付回调后的参数prepay_id: {}".format(prepay_id))
            except Exception as e:
                return Response ( {'code': 1002, 'msg': '订单号重复'}, status=status.HTTP_400_BAD_REQUEST )
            timeStamp = str ( int ( time.time () ) )

            data = {
                "appId": APP_ID,
                "nonceStr": nonce_str,
                "package": "prepay_id=" + prepay_id,
                "signType": 'MD5',
                "timeStamp": timeStamp
            }
            # 再次签名
            paySign = WXUtils.wx_sign ( data )
            data[ 'paySign' ] = paySign
            data[ 'out_trade_no' ] = out_trade_no
            data[ 'code' ] = 'success'
            return Response ( data )

        else:
            return Response ( {'code': 1002}, status=status.HTTP_400_BAD_REQUEST )


# 支付结果
class PayResult ( APIView ):
    """支付结果"""

    # 微信推送支付结果
    def post ( self, request ):
        _xml = request.body
        # 拿到微信发送的xml请求 即微信支付后的回调内容
        xml = str ( _xml, encoding="utf-8" )
        print("xml", xml)
        return_dict = {}
        tree = et.fromstring ( xml )
        # xml 解析
        return_code = tree.find ( "return_code" ).text
        result_code = tree.find ( "result_code" ).text

        try:
            if return_code == 'FAIL':
                # 官方发出错误
                print('回调失败FAIL')
                return_dict['out_trade_no'] = tree.find ( "out_trade_no" ).text
                return_dict[ 'message' ] = tree.find ( "err_code_des" ).text
                return_dict['code'] = tree.find ( "err_code" ).text
                return Response(return_dict)
            elif return_code == 'SUCCESS' and result_code == "SUCCESS":
                return_dict = {
                    'code':200,
                    'message':result_code,
                    'out_trade_no':tree.find ( "out_trade_no" ).text,
                }
                out_trade_no = tree.find ( "out_trade_no" ).text
                data = wxpay.order_query ( out_trade_no=out_trade_no )
                _out_trade_no = tree.find ( "out_trade_no" ).text
                # 这里省略了 拿到订单号后的操作 看自己的业务需求
                print(_out_trade_no,"支付成功订单号,异步接收")
                # 拿到自己这次支付的 out_trade_no
                order = OrderInfo.objects.get ( order_sn=out_trade_no )
                # 更改订单状态为支付成功
                order.status = 2
                order.save ()
                # 并累加商品销量值
                spu = SPU.objects.get ( spu_code=order.goods_spu )
                sales = order.total_count
                spu.sales = sales + spu.sales
                spu.save ()
                number = GoodsNumbers.objects.get ( goodsNumber_id=order.goodsNumber, goods_size=order.size )
                stock = number.goods_sales
                number.goods_sales = stock + order.total_count
                number.save ()
                id = order.user_id # 获取订单的买家id
                # 查询买家信息记录
                buyer_id = User.objects.get(id=order.user_id)
                # 查询用户的级别邀请人信息
                user = USerDetailRank.objects.get ( type_id=id )
                if user.pid != 0:
                    try:

                        # 查询 看是否是特邀二级,并获取佣金利率
                        openids = User.objects.get ( id=user.pid )
                        # print("openid: ",openids.ZGVIP_code)
                        openid = openids.ZGVIP_code
                        merchant = Merchant.objects.get ( wx_id=openid )
                        gain_section = decimal.Decimal ( int ( merchant.gain_section ) / 100 )
                        # print("特邀: gain_section",gain_section)
                        # 查询三级邀请人是否存在
                        try:
                            invtie = USerDetailRank.objects.get ( type_id=user.pid ).pid
                            # 获取到 三级的利率是多少
                            invites = User.objects.get ( id=invtie )
                            count = (invites.invite_count + invites.rase_base)
                            # 查出对应的利率
                            ladder = Ladder.objects.all ().order_by ( 'create_time' )
                            ladderList = [ ]
                            for i in ladder:
                                dicts = {}
                                dicts[ 'id' ] = i.id
                                dicts[ 'ladder_section' ] = i.ladder_section
                                ladderList.append ( dicts )
                            if int ( count ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
                                gain = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=3 ).gain
                                # 三级的利率
                            elif int ( count ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
                                gain = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=3 ).gain
                                # 三级的利率
                            else:
                                gain = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=3 ).gain
                                # 三级的利率
                            gain = decimal.Decimal ( int ( gain ) / 100 )
                            zgvip2 = User.objects.get (id=order.invite_user_id )
                            Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
                                                        buyer_wx_name=order.user_nickname,
                                                        actual_payment=order.actual_payment, goods_name=order.goods_name,
                                                        payment_time=order.payment_time, commission_status=1,
                                                        up_beneficimary=order.invite_nickname,
                                                        up_wx_user_id=zgvip2.ZGVIP_code,
                                                        up_gain_money=(gain_section * order.actual_payment),
                                                        up_up_beneficimary=invites.nickName,
                                                        up_up_wx_user_id=invites.ZGVIP_code,
                                                        up_up_gain=(gain * order.actual_payment)
                                                        ).save ()
                            # print("有三级: ",(gain_section * order.actual_payment))
                            zgvip2.onroad += (gain_section * order.actual_payment)
                            zgvip3 = User.objects.get (id=zgvip2.invite_user_id )
                            zgvip3.onroad += (gain * order.actual_payment)
                            zgvip3.save()
                            zgvip2.save()
                        except:
                            zgvip = User.objects.get (id=order.invite_user_id )
                            Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
                                                        buyer_wx_name=order.user_nickname,
                                                        actual_payment=order.actual_payment, goods_name=order.goods_name,
                                                        payment_time=order.payment_time, commission_status=1,
                                                        up_beneficimary=order.invite_nickname,
                                                        up_wx_user_id=zgvip.ZGVIP_code,
                                                        up_gain_money=(gain_section * order.actual_payment),
                                                        up_up_beneficimary=0,
                                                        up_up_wx_user_id=0, up_up_gain=0
                                                        ).save ()
                            # print("没有三级: ",(gain_section * order.actual_payment))
                            zgvip.onroad += (gain_section * order.actual_payment)
                            zgvip.save()
                    except:
                        count = int (
                            User.objects.get ( id=user.pid ).invite_count + User.objects.get ( id=user.pid ).raise_base )
                        ladder = Ladder.objects.all ().order_by ( 'create_time' )
                        ladderList = [ ]
                        for i in ladder:
                            dicts = {}
                            dicts[ 'id' ] = i.id
                            dicts[ 'ladder_section' ] = i.ladder_section
                            ladderList.append ( dicts )
                        if int ( count ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
                            gain_section = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=2 ).gain
                            # 2级的利率
                        elif int ( count ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
                            gain_section = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=2 ).gain
                            # 2级的利率
                        else:
                            gain_section = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=2 ).gain
                            # 2级的利率
                        gain_section = decimal.Decimal ( int ( gain_section ) / 100 )
                    try:
                        invtie = USerDetailRank.objects.get ( type_id=user.pid ).pid  # 获取 top_id
                        # 获取到 三级的利率是多少
                        invites = User.objects.get ( id=invtie )  # 查询user 表中的 邀请数量
                        # print(invites,'三级user')
                        counts = invites.invite_count + invites.raise_base
                        # 查出对应的利率
                        # print(counts,'销量基数')
                        ladder = Ladder.objects.all ().order_by ( 'create_time' )
                        ladderList = [ ]
                        for i in ladder:
                            dicts = {}
                            dicts[ 'id' ] = i.id
                            dicts[ 'ladder_section' ] = i.ladder_section
                            ladderList.append ( dicts )
                        # 三级的利率
                        if int ( counts ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
                            gain = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=3 ).gain
                        elif int ( counts ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
                            gain = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=3 ).gain
                        else:
                            gain = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=3 ).gain
                        gain = decimal.Decimal ( int ( gain ) / 100 )
                        zgvip4 = User.objects.get (id=order.invite_user_id )
                        zgvip5 = User.objects.get (id=zgvip4.invite_user_id )
                        Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
                                                    buyer_wx_name=order.user_nickname,
                                                    actual_payment=order.actual_payment, goods_name=order.goods_name,
                                                    payment_time=order.payment_time, commission_status=1,
                                                    up_beneficimary=order.invite_nickname,
                                                    up_wx_user_id=zgvip4.ZGVIP_code,
                                                    up_gain_money=(gain_section * order.actual_payment),
                                                    up_up_beneficimary=invites.nickName,
                                                    up_up_wx_user_id=invites.ZGVIP_code,
                                                    up_up_gain=(gain * order.actual_payment)
                                                    ).save ()
                        zgvip4.onroad += (gain_section * order.actual_payment)
                        zgvip5.onroad += (gain * order.actual_payment)
                        zgvip4.save()
                        zgvip5.save()
                    except:
                        # print('ex erorr')
                        zgvip4 = User.objects.get (id=order.invite_user_id )
                        Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
                                                    buyer_wx_name=order.user_nickname,
                                                    actual_payment=order.actual_payment, goods_name=order.goods_name,
                                                    payment_time=order.payment_time, commission_status=1,
                                                    up_beneficimary=order.invite_nickname,
                                                    up_wx_user_id=zgvip4.ZGVIP_code,
                                                    up_gain_money=(gain_section * order.actual_payment),
                                                    up_up_beneficimary='',
                                                    up_up_wx_user_id=0, up_up_gain=0
                                                    ).save ()
                        zgvip4.onroad += (gain_section * order.actual_payment)
                        zgvip4.save()
                else:
                    pass
                # 刷新缓存
                redis_conn = get_redis_connection ( 'mySession' )
                redis_conn.set ( 'mySession_%s' % request.user.id, pickle.dumps ( user ), 30 * 60 * 60 )
        except Exception as e:
            print(e)
        finally:
            return Response ( return_dict )

    # 确认收货
    def put ( self, request ):
        out_trade_no = request.data[ 'out_trade_no' ].strip ()
        # print ( out_trade_no, '订单号' )
        # 获取订单信息, 并改变订单状态为 已完成
        order = OrderInfo.objects.get ( order_sn=out_trade_no )
        order.status = 5
        order.save ()
        # 判断 订单是否存在上级
        if order.invite_user_id != 0:
            # 存在 改变状态为已完成
            G = Commission.objects.get ( order_num=out_trade_no )
            G.commission_status = 2
            # 需要查询 二级三级信息  对邀请人的金额进行修改....
            user = User.objects.get ( id=order.user_id )
            # 获取用户上级信息 对二级 的在途货款和已到账货款做修改,已经分享的真实数量累加
            invite = User.objects.get ( id=user.invite_user_id )
            invite.invite_count += order.total_count
            invite.onroad -= G.up_gain_money
            invite.balance += G.up_gain_money
            invite.save ()
            if invite.invite_user_id != 0:
                # print ( 4 )
                up_invite = User.objects.get ( id=invite.invite_user_id )
                up_invite.invite_count += order.total_count
                up_invite.onroad -= G.up_up_gain
                up_invite.balance += G.up_up_gain
                up_invite.save ()
        return Response ( {'code': 200, 'msg': '{}以确认收货'.format ( out_trade_no )}, status=status.HTTP_200_OK )


class PayReturn ( APIView ):
    """支付成功分流"""

    def post ( self, request ):
        _status = json.loads ( request.body )
        out_trade_no = _status[ "out_trade_no" ]
        data = wxpay.order_query ( out_trade_no=out_trade_no )
        msg = {"cash_fee": data[ 'cash_fee' ],
               'out_trade_no': data[ 'out_trade_no' ],
               'trade_state': data[ 'trade_state' ],
               "code": 200,
               "msg": "success"}
        # if data[ 'trade_state' ] == 'SUCCESS':
        #     # 拿到自己这次支付的 out_trade_no
        #     order = OrderInfo.objects.get ( order_sn=out_trade_no )
        #     # 更改订单状态为支付成功
        #     order.status = 2
        #     order.save ()
        #     # 并累加商品销量值
        #     spu = SPU.objects.get ( spu_code=order.goods_spu )
        #     sales = order.total_count
        #     spu.sales = sales + spu.sales
        #     spu.save ()
        #     number = GoodsNumbers.objects.get ( goodsNumber_id=order.goodsNumber, goods_size=order.size )
        #     stock = number.goods_sales
        #     number.goods_sales = stock + order.total_count
        #     number.save ()
        #     id = order.user_id # 获取订单的买家id
        #     # 查询买家信息记录
        #     buyer_id = User.objects.get(id=order.user_id)
        #     # 查询用户的级别邀请人信息
        #     user = USerDetailRank.objects.get ( type_id=id )
        #     if user.pid != 0:
        #         try:

        #             # 查询 看是否是特邀二级,并获取佣金利率
        #             openids = User.objects.get ( id=user.pid )
        #             print("openid: ",openids.ZGVIP_code)
        #             openid = openids.ZGVIP_code
        #             merchant = Merchant.objects.get ( wx_id=openid )
        #             gain_section = decimal.Decimal ( int ( merchant.gain_section ) / 100 )
        #             print("特邀: gain_section",gain_section)
        #             # 查询三级邀请人是否存在
        #             try:
        #                 invtie = USerDetailRank.objects.get ( type_id=user.pid ).pid
        #                 # 获取到 三级的利率是多少
        #                 invites = User.objects.get ( id=invtie )
        #                 count = (invites.invite_count + invites.rase_base)
        #                 # 查出对应的利率
        #                 ladder = Ladder.objects.all ().order_by ( 'create_time' )
        #                 ladderList = [ ]
        #                 for i in ladder:
        #                     dicts = {}
        #                     dicts[ 'id' ] = i.id
        #                     dicts[ 'ladder_section' ] = i.ladder_section
        #                     ladderList.append ( dicts )
        #                 if int ( count ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
        #                     gain = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=3 ).gain
        #                     # 三级的利率
        #                 elif int ( count ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
        #                     gain = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=3 ).gain
        #                     # 三级的利率
        #                 else:
        #                     gain = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=3 ).gain
        #                     # 三级的利率
        #                 gain = decimal.Decimal ( int ( gain ) / 100 )
        #                 zgvip2 = User.objects.get (id=order.invite_user_id )
        #                 Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
        #                                             buyer_wx_name=order.user_nickname,
        #                                             actual_payment=order.actual_payment, goods_name=order.goods_name,
        #                                             payment_time=order.payment_time, commission_status=1,
        #                                             up_beneficimary=order.invite_nickname,
        #                                             up_wx_user_id=zgvip2.ZGVIP_code,
        #                                             up_gain_money=(gain_section * order.actual_payment),
        #                                             up_up_beneficimary=invites.nickName,
        #                                             up_up_wx_user_id=invites.ZGVIP_code,
        #                                             up_up_gain=(gain * order.actual_payment)
        #                                             ).save ()
        #                 print("有三级: ",(gain_section * order.actual_payment))
        #                 zgvip2.onroad += (gain_section * order.actual_payment)
        #                 zgvip3 = User.objects.get (id=zgvip2.invite_user_id )
        #                 zgvip3.onroad += (gain * order.actual_payment)
        #                 zgvip3.save()
        #                 zgvip2.save()
        #             except:
        #                 zgvip = User.objects.get (id=order.invite_user_id )
        #                 Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
        #                                             buyer_wx_name=order.user_nickname,
        #                                             actual_payment=order.actual_payment, goods_name=order.goods_name,
        #                                             payment_time=order.payment_time, commission_status=1,
        #                                             up_beneficimary=order.invite_nickname,
        #                                             up_wx_user_id=zgvip.ZGVIP_code,
        #                                             up_gain_money=(gain_section * order.actual_payment),
        #                                             up_up_beneficimary=0,
        #                                             up_up_wx_user_id=0, up_up_gain=0
        #                                             ).save ()
        #                 print("没有三级: ",(gain_section * order.actual_payment))
        #                 zgvip.onroad += (gain_section * order.actual_payment)
        #                 zgvip.save()
        #         except:
        #             count = int (
        #                 User.objects.get ( id=user.pid ).invite_count + User.objects.get ( id=user.pid ).raise_base )
        #             ladder = Ladder.objects.all ().order_by ( 'create_time' )
        #             ladderList = [ ]
        #             for i in ladder:
        #                 dicts = {}
        #                 dicts[ 'id' ] = i.id
        #                 dicts[ 'ladder_section' ] = i.ladder_section
        #                 ladderList.append ( dicts )
        #             if int ( count ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
        #                 gain_section = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=2 ).gain
        #                 # 2级的利率
        #             elif int ( count ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
        #                 gain_section = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=2 ).gain
        #                 # 2级的利率
        #             else:
        #                 gain_section = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=2 ).gain
        #                 # 2级的利率
        #             gain_section = decimal.Decimal ( int ( gain_section ) / 100 )
        #         try:
        #             invtie = USerDetailRank.objects.get ( type_id=user.pid ).pid  # 获取 top_id
        #             # 获取到 三级的利率是多少
        #             invites = User.objects.get ( id=invtie )  # 查询user 表中的 邀请数量
        #             print(invites,'三级user')
        #             counts = invites.invite_count + invites.raise_base
        #             # 查出对应的利率
        #             print(counts,'销量基数')
        #             ladder = Ladder.objects.all ().order_by ( 'create_time' )
        #             ladderList = [ ]
        #             for i in ladder:
        #                 dicts = {}
        #                 dicts[ 'id' ] = i.id
        #                 dicts[ 'ladder_section' ] = i.ladder_section
        #                 ladderList.append ( dicts )
        #             # 三级的利率
        #             if int ( counts ) <= int ( ladderList[ 0 ][ 'ladder_section' ] ):
        #                 gain = RankSell.objects.get ( ladder=ladderList[ 0 ][ 'id' ], rank=3 ).gain
        #             elif int ( counts ) <= int ( ladderList[ 1 ][ 'ladder_section' ] ):
        #                 gain = RankSell.objects.get ( ladder=ladderList[ 1 ][ 'id' ], rank=3 ).gain
        #             else:
        #                 gain = RankSell.objects.get ( ladder=ladderList[ -1 ][ 'id' ], rank=3 ).gain
        #             gain = decimal.Decimal ( int ( gain ) / 100 )
        #             zgvip4 = User.objects.get (id=order.invite_user_id )
        #             zgvip5 = User.objects.get (id=zgvip4.invite_user_id )
        #             Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
        #                                         buyer_wx_name=order.user_nickname,
        #                                         actual_payment=order.actual_payment, goods_name=order.goods_name,
        #                                         payment_time=order.payment_time, commission_status=1,
        #                                         up_beneficimary=order.invite_nickname,
        #                                         up_wx_user_id=zgvip4.ZGVIP_code,
        #                                         up_gain_money=(gain_section * order.actual_payment),
        #                                         up_up_beneficimary=invites.nickName,
        #                                         up_up_wx_user_id=invites.ZGVIP_code,
        #                                         up_up_gain=(gain * order.actual_payment)
        #                                         ).save ()
        #             zgvip4.onroad += (gain_section * order.actual_payment)
        #             zgvip5.onroad += (gain * order.actual_payment)
        #             zgvip4.save()
        #             zgvip5.save()
        #         except:
        #             print('ex erorr')
        #             zgvip4 = User.objects.get (id=order.invite_user_id )
        #             Commission.objects.create ( order_num=out_trade_no, buyer=buyer_id.ZGVIP_code,
        #                                         buyer_wx_name=order.user_nickname,
        #                                         actual_payment=order.actual_payment, goods_name=order.goods_name,
        #                                         payment_time=order.payment_time, commission_status=1,
        #                                         up_beneficimary=order.invite_nickname,
        #                                         up_wx_user_id=zgvip4.ZGVIP_code,
        #                                         up_gain_money=(gain_section * order.actual_payment),
        #                                         up_up_beneficimary='',
        #                                         up_up_wx_user_id=0, up_up_gain=0
        #                                         ).save ()
        #             zgvip4.onroad += (gain_section * order.actual_payment)
        #             zgvip4.save()
        #     else:
        #         pass
        #     # 刷新缓存
        #     redis_conn = get_redis_connection ( 'myUser_Id_' )
        #     redis_conn.set ( 'myUserId_%s' % request.user.id, pickle.dumps ( user ), 30 * 60 * 60 )
        return Response ( msg )


class WXUtils ( object ):
    """关于微信支付的小工具"""

    # 随机32位字符串
    @staticmethod
    def randomStr ():
        return ''.join ( random.sample ( string.ascii_letters + string.digits, 32 ) )

    # 微信签名算法函数
    @staticmethod
    def wx_sign ( param ):
        stringA = ""
        ks = sorted ( param.keys () )
        # 排序
        for k in ks:
            stringA += (k + "=" + str ( param[ k ] ) + "&")
        # 拼接商户key
        stringSignTemp = stringA + 'key=' + APP_PARTNER_KEY
        # md5加密
        hash_md5 = hashlib.md5 ( stringSignTemp.encode ( 'utf-8' ) )
        sign = hash_md5.hexdigest ().upper ()
        return sign

    # 发送xml请求
    @staticmethod
    def send_xml_request ( url, param ):
        param = {'xml': param}
        xml = xmltodict.unparse ( param )
        print(xml.encode('utf-8'))
        response = requests.post ( url, data=xml.encode ( "utf-8" ), headers={"Content-Type": "charset=utf-8"} )
        msg = response.content
        xmlmsg = xmltodict.parse ( msg )
        return xmlmsg


