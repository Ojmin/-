from django.conf.urls import url

from . import views

urlpatterns = [
    # 确认订单
    # url(r'^orders/settlement/$', views.OrderSettlementView.as_view()),
    # # 提交订单
    url(r'^orderView', views.OrderView.as_view()),
    url(r'^logistics', views.LogisticsView.as_view()),
	url('api/v1/notifications', views.notifications),
    url(r'^orderDetail', views.OrderDetail.as_view()),
    url(r'^$', views.Index.as_view()),
    url(r'^userwith', views.UserWithdrawcash.as_view()),
    url(r'^reuse_refund', views.RefundList.as_view()),
    # url(r'^refund', views.RefundAPI.as_view()),
]
