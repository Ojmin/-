from django.conf.urls import url

from . import views

urlpatterns = [
    # 预支付
    url(r'^refund', views.Refund.as_view()),
    url(r'^detail_refund', views.RefundDetail.as_view()),
    url(r'^off_order', views.OffOrder.as_view()),
    url(r'^wuliu_refund', views.RefundWuLiu.as_view()),

]
