from django.contrib.auth.backends import ModelBackend

from django.contrib.auth.models import User
from rest_framework.views import APIView


def get_user_by_account(account):
    """
    根据用户名或者手机号查询用户
    :param account: 用户名或者手机号
    :return: user/None
    """

    try:
        user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    """自定义用户认证后端"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        根据username(此时表示用户名，主要是账号)
        :param request: 本次登录请求
        :param username:用户名
        :param password: 密码明文
        :param kwargs: 额外参数
        :return: user
        """
        # 使用账号或者手机号查询用户
        user = get_user_by_account(username)

        # 如果用户存在，就校验密码，密码正确就返回user
        if user and user.check_password(password):
            return user
        else:
            return
