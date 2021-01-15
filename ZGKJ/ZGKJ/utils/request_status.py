import os
import requests
import redis,json
from aiohttp.web_protocol import RequestHandler
import redis
# 抽取封装成模块，全局使用（单例模式，redis_pool.py）
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=1000, decode_responses=True)
template_id = 'BzHz-BZFkFWP2L4BdsboFVPwHcLPpEIUwF4kZ1dKIH8'
APPID = 'wx45221ea345e0df25'
APPSECRET = 'da330c40d0aa71334909fb7a5d04812e'



def get_access_token():
    payload = {
    'grant_type': 'client_credential',
    'appid': APPID,
    'secret': APPSECRET
    }

    req = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=payload, timeout=3, verify=False)
    access_token = req.json().get('access_token')
    # 建立reids连接
    conn = redis.Redis ( connection_pool=POOL )
    # 保存redis并返回给前端
    conn.set('ACCESS_TOKEN', access_token)
    print(access_token)



# class FormHandler(RequestHandler):
#
#     def post(self):
#         # req_data = self.request.body
#         # req_data = json.loads(req_data)
#         # form_id = req_data.get('form_id')
#         template_push(template_id)  # 使用消息进行模板推送
#
#
#
# def template_push(form_id):
#     data = {
#         "touser": 'o4uDc4j93DKMa4N0eqaMZvYe99aQ',
#         "template_id": template_id,
#         "page": 'pages/index/index',
#         "form_id": form_id,
#         "data": {
#             'keyword1': {
#                 'value': 'value1'
#             }
#         },
#         "emphasis_keyword": ''
#     }
#     conn = redis.Redis ( connection_pool=POOL )
#     access_token = conn.get('ACCESS_TOKEN')
#     push_url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}'.format(access_token)
#     requests.post(push_url, json=data, timeout=3, verify=False)
#
# if __name__ == '__main__':
#     get_access_token()
#!/usr/bin/env python
# _*_coding:utf-8 _*_

import pika
import sys
import time

# 远程rabbitmq服务的配置信息
username = 'admin'  # 指定远程rabbitmq的用户名密码
pwd = 'root'
ip_addr = '106.13.207.205'
port_num = 5672

credentials = pika.PlainCredentials ( username, pwd )
connection = pika.BlockingConnection ( pika.ConnectionParameters ( ip_addr, port_num, '/', credentials ) )
channel = connection.channel ()


# 消费成功的回调函数
def callback ( ch, method, properties, body ):
    print ( " [%s] Received %r" % (time.time (), body) )
    # time.sleep(0.2)


# 开始依次消费balance队列中的消息
channel.basic_consume ( queue='balance', on_message_callback=callback, auto_ack=True )

print ( ' [*] Waiting for messages. To exit press CTRL+C' )
channel.start_consuming ()  # 启动消费