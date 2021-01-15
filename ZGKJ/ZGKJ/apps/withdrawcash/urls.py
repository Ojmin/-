from django.conf.urls import url

from withdrawcash import views

urlpatterns = [

    # 提现
    url(r'^businessPayOrder', views.WithdrawCash.as_view()),
    url(r'^businessPay', views.BusinessPay.as_view()),
    url(r'^invitation', views.InvitationInfo.as_view()),
    url(r'^user_wallet', views.UserInfoView.as_view()),

]