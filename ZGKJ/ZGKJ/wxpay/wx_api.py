from django.contrib import admin
from django.urls import path
from ZGKJ.wxpay import api,wx_api

urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/',api.wx_login),
    path('wx_pay/',wx_api.wx_login)
]