"""ZGKJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
#import xadmin
from django.conf import settings
from django.views import static
from rest_framework.routers import DefaultRouter

import backstage
from goods import views

urlpatterns = [
    # xadmin
 #   url(r'^ckeditor/', include('ckeditor_uploader.urls')),
  #  url('xadmin/', include(xadmin.site.urls)),
    # 逻辑
    url('goods/', include('goods.urls')),
    url('users/', include('users.urls')),
    url(r'^', include('orders.urls')),
    url(r'^', include('areas.urls')),
    url(r'^', include('payment.urls')),
    url(r'^', include('refund.urls')),
    url(r'^', include('withdrawcash.urls')),
    # 静态文件 测试用的
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
]
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT
#         }),
#     ]
router = DefaultRouter()
router.register('search', views.SPUSearchViewSet, base_name='skus_search')

urlpatterns += router.urls
