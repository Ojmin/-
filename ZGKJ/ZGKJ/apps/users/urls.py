from django.conf.urls import url

from . import views

urlpatterns = [
    # 商品列表
    # url(r'^/', views.SKUListView.as_view()),

    # 测试商品详情的查询代码
    url(r'^login', views.WXLoginView.as_view()),
    url(r'^star', views.UserStarList.as_view()),
    url(r'^userInfo', views.UserCenter.as_view()),
    url(r'^special_agent', views.SpecialAgent.as_view()),
    url(r'^token_true', views.WeiXinToken.as_view()),


]
# router = routers.DefaultRouter()
# router.register(r'addresses', views.AddressViewSet, base_name='addresses')
#
# urlpatterns += router.urls
# POST /addresses/ 新建  -> create
# PUT /addresses/<pk>/ 修改  -> update
# GET /addresses/  查询  -> list
# DELETE /addresses/<pk>/  删除 -> destroy
# PUT /addresses/<pk>/status/ 设置默认 -> status
# PUT /addresses/<pk>/title/  设置标题 -> title
