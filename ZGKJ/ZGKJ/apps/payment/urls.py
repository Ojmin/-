from django.conf.urls import url

from . import views

urlpatterns = [
    # 预支付
    url(r'^payView', views.PayView.as_view()),
    url(r'^payResult', views.PayResult.as_view()),
    url(r'^payReturn', views.PayReturn.as_view()),
]
