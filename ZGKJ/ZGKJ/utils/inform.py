import requests
import redis
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=1000, decode_responses=True)


# from ZGKJ.utils.redis_pool import POOL
# from ZGKJ.settings.dev import APPID,APPSECRET
APP_ID = 'wx45221ea345e0df25'
APP_SECRET = '31c9da1a09c8b354d45510388a90fc03'
#获取access_token并保存到redis库中
def index ():
    conn = redis.Redis ( connection_pool=POOL )
    response = requests.get (
        'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format ( APP_ID,APP_SECRET ) )
    response = response.json ()
    print(response)
    if response.get ( 'access_token', '' ):
        print(response.get ( 'access_token', '' ))
        conn.set ( 'access_token', response[ 'access_token' ] )
        conn.expire ( 'access_token',7200)
    return  ( '设置成功' )


def order ():
    conn = redis.Redis ( connection_pool=POOL )
    access_token = conn.get ( 'access_token' )
    import json
    return   str(access_token,encoding='utf-8')
if __name__ == '__main__':
    print(index())
    print(order())