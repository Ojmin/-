import datetime, jwt, time
import logging

logger = logging.getLogger('django')


class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=7*24),
                'iat': datetime.datetime.utcnow(),
                'id': user_id,
                'login_time': login_time
            }
            return jwt.encode(
                payload,
                'zg_secret',
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, 'zg_secret', options={'verify_exp': True})
            if ('id' in payload):
                # return payload
                return payload["id"]
            else:
                return False

        except Exception as e:
            logger.info(e)
            return False


if __name__ == '__main__':
    print(Auth.encode_auth_token(1,"fsf"))
    'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzU0NDE2NjYsImlhdCI6MTU3NTQ0MTM2NiwiaWQiOjE1LCJsb2dpbl90aW1lIjoiZnNmIn0.sJMrsl_5t9X3TqtmpJOAaAJdW3ANXV7bhtif2eOKH4o'
