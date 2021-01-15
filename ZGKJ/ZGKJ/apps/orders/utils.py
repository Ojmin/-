import requests

from ZGKJ.settings.dev import APP_CODE, LOGISTICS_URL

#查询物流信息接口
def enquiry_logistics(logistics_no, company_no=None):
    """请求物流信息"""
    appcode = APP_CODE
    params = {'no': logistics_no, 'type': company_no}

    url = LOGISTICS_URL
    headers = {'Authorization': 'APPCODE ' + appcode}
    r = requests.get(url, headers=headers, params=params)
    return r.text


if __name__ == '__main__':
    print(enquiry_logistics('773023253870120'))
