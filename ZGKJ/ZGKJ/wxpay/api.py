from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import requests
import hashlib
import xmltodict
import time
import datetime
import random
import string

# openid地址 get请求
openIdUrl = 'https://api.weixin.qq.com/sns/jscode2session'
# 统一下单url
toOrderUrl = 'https://api.mch.weixin.qq.com/pay/unifiedorder'

wxinfo = {
    "APPID": "",
    "SECRET": "",
    "MCHID": "",
    "MCHKEY": ""
}


@api_view(['GET'])
def wx_login(request):
    code = request.GET['code']  # wxlogin()获取的code
    res = requests.get(
        url=openIdUrl,
        params={
            'appid': wxinfo['APPID'],
            'secret': wxinfo['SECRET'],
            'js_code': code,
            'grant_type': 'authorization_code'
        }
    ).json()
    openid = res['openid']  # 存储到用户模型中

    now_time = datetime.datetime.now()
    out_trade_no = str(now_time.year) + str(now_time.month) + str(now_time.day) + str(
        random.randrange(100000, 999999)) + str(random.randrange(1000, 9999))
    nonce_str = randomStr()
    params = {
        'appid': wxinfo['APPID'],
        'mch_id': wxinfo['MCHID'],
        'nonce_str': nonce_str,
        # 'sign':sign,
        'body': "",  # 商品描述，通过request对象获取，前端传过来
        "out_trade_no": out_trade_no,
        "total_fee": '1000',  # 单位分，金额
        "spbill_create_ip": "47.123.123.123",  # 服务器地址
        "notify_url": "",  # 支付成功的回馈地址
        "trade_type": "JSAPI",  # 交易类型 小程序定死jsapi
        "openid": openid
    }
    sign = wx_sign(params)
    params['sign'] = sign
    xmlmsg = send_xml_request(toOrderUrl, params)
    if xmlmsg['xml']['return_code'] == 'SUCCESS':
        prepay_id = xmlmsg['xml']['prepay_id']
        timeStamp = str(int(time.time()))

        data = {
            "appId": wxinfo['APPID'],
            "nonceStr": nonce_str,
            "package": "prepay_id=" + prepay_id,
            "signType": 'MD5',
            "timeStamp": timeStamp
        }
        # 再次签名
        paySign = wx_sign(data)
        data['payign'] = paySign
    return Response(data)


# 随机32位字符串
def randomStr():
    return ''.join(random.sample(string.ascii_letters + string.digits, 32))


# 微信签名算法函数
def wx_sign(param):
    stringA = ""
    ks = sorted(param.keys())
    # 排序
    for k in ks:
        stringA += (k + "=" + param[k] + "&")
    # 拼接商户key
    stringSignTemp = stringA + 'key=' + wxinfo['MCHKEY']
    # md5加密
    hash_md5 = hashlib.md5(stringSignTemp.encode('utf-8'))
    sign = hash_md5.hexdigest().upper()
    return sign


# 发送xml请求
def send_xml_request(url, param):
    param = {'xml': param}
    xml = xmltodict.unparse(param)  #xmltodict.unparse() 将字典转成xml 字符串
    response = requests.post(url, data=xml.encode("utf-8"), headers={"Content-Type": "charset=utf-8"})
    msg = response.text
    xmlmsg = xmltodict.parse(msg)  #xmltodict.parse()将xml数据转为python中的dict字典数据
    return xmlmsg
