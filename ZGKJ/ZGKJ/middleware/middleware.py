import pickle

import jwt
from django.shortcuts import render_to_response
from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection
from rest_framework import status

from django.http import JsonResponse

from goods.models import User
from verification.views import Auth


class JWTMiddleware(MiddlewareMixin):

    def process_request(self, request):

        url = request.get_full_path()
        if ('token_true' in url) or ('login' in url) or ('goods' in url) or ('media' in url):
            pass
        else:
            auth_jwt = request.META.get('HTTP_AUTHORIZATION')

            if auth_jwt:
                try:
                    payload = jwt.decode(auth_jwt.encode('utf-8'), 'zg_secret', options={'verify_exp': True})
                    if ('id' in payload and 'login_time' in payload):
                        pass
                    else:
                        raise jwt.InvalidTokenError
                except jwt.ExpiredSignatureError:
                    return JsonResponse({'error': "Token过期"}, status=status.HTTP_401_UNAUTHORIZED)

                except jwt.InvalidTokenError:
                    return JsonResponse({'error': "无效的Token"}, status=status.HTTP_401_UNAUTHORIZED)


                except Exception:
                    return JsonResponse({'error': "非法Token"}, status=status.HTTP_401_UNAUTHORIZED)

            else:
                return JsonResponse({'error': '没有提供认证token'}, status=status.HTTP_401_UNAUTHORIZED)


class CorsMiddleware(MiddlewareMixin):
    '''
    解决跨域问题
    '''
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "*"
        response["Access-Control-Allow-Headers"] = "Content-Type, userid"
        return response


class UserIdVerify(MiddlewareMixin):
    '''
    用户未登录访问接口
    '''
    def process_request(self, request):
        print("请求")
        print(request)
        if request.method == 'OPTIONS':
            return JsonResponse({'msg': 'ok'}, status=status.HTTP_200_OK)
        url = request.get_full_path()
        print('进入验证: ',url)
        filter_url = ['xadmin', 'login', 'html', 'media', 'ckeditor', 'payResult', 'attendant', 'goodsPoint',
                      'goodsDetail', "goods_detail", 'goods_recommend', "goods_hot", 'goods_new', "goods_list",
                      'search', 'banner_show', 'goods_star', 'icon_show','show_icon_goods', 'block_show','show_block_goods','token_true']
        if True in [i in url for i in filter_url] or url == '/':
            print('无拦截')
            return None
        else:
            print('进入拦截')
            try:
                # 获取头部信息中的 userid
                request.user_id = int(request.META.get('HTTP_USERID'))
            except:
                return render_to_response('404.html')
            try:
                # 获取头部信息中的 token串
                token = request.META.get('HTTP_AUTHORIZATION')
                # print(token)
                if not Auth.decode_auth_token(token):
                    return JsonResponse({"code": 10006, "msg": "token_false"})
                request.user_id = Auth.decode_auth_token(token)
            except Exception as e:
                # print(e)
                return JsonResponse({"msg": "没有token", "code": 10006})
            # 获取原始settings 中的 redis 助手
            redis_conn = get_redis_connection('mySession')

            # 缓存用户 过期30分钟
            wx_user = redis_conn.get('mySession_%s' % request.user_id)
            if wx_user:
                request.wx_user = pickle.loads(wx_user)# pickle转存储程序
            else:
                try:
                    request.wx_user = User.objects.get(id=request.user_id)

                except Exception as e:
                    # print(e)
                    return JsonResponse({'error_message': '没有该用户，请重新登录', 'error_code': '01'},
                                        status=10006)
                else:
                    # print(request.wx_user)
                    redis_conn.set('mySession_%s' % request.wx_user.id, pickle.dumps(request.wx_user), 24 * 60 * 60)

            # try:
            #     request.wx_user = User.objects.get(id=request.user_id)
            # except Exception as e:
            #     return JsonResponse({'error_message': '没有该用户，请重新登录', 'error_code': '01'},
            #                         status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     pass
