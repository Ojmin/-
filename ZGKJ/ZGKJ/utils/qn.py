# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag
import qiniu.config


def upload(goodsNumber):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'PzGOinITN_nvblC94u9IwiitOAdcWpzjJAWVBjti'
    secret_key = 'qb21ulP4ozR1yoLg97NG339Jh_dV9A0hFcExdWjQ'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'zgkj'

    # 上传后保存的文件名
    key = '%s.png' % goodsNumber

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    localfile = '../moxing/{}.jpg'.format(goodsNumber)

    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


if __name__ == '__main__':
    upload('fjfj-190')
