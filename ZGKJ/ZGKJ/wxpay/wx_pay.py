from rest_framework.views import APIView
from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt
from rest_framework.response import Response

APP_ID = 'wx45221ea345e0df25'
APP_SECRET = 'da330c40d0aa71334909fb7a5d04812e'
api = WXAPPAPI(appid=APP_ID,
               app_secret=APP_SECRET)


class WXLoginView(APIView):
    def get(self, request):
        code = request.GET['code']
        encrypted_data = request.GET['encrypted_data']
        iv = request.GET['iv']
        session_info = api.exchange_code_for_session_key(code=code)

# 获取session_info 后

        session_key = session_info.get('session_key')
        crypt = WXBizDataCrypt(APP_ID, session_key)

# encrypted_data 包括敏感数据在内的完整用户信息的加密数据
# iv 加密算法的初始向量
# 这两个参数需要js获取
        user_info = crypt.decrypt(encrypted_data, iv)
        print(user_info)
        return Response('ok')
