from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    # 商品列表
    # url(r'^/', views.SKUListView.as_view()),


    # 测试商品详情的查询代码

    url(r'^goods_detail', views.SPUView.as_view()),
    url(r'^goodsDetail', views.GoodsDetail.as_view()),
    # url(r'^money', views.BuyView.as_view()),
    url(r'^category', views.CategoryView.as_view()),
    url(r'^goodsPoint', views.GoodsPointView.as_view()),
    url(r'^upload', views.QiniuUpload.as_view()),

    url(r'^goods_list', views.GoodsListView.as_view()),
     # 小程序首页接口
    url(r'^goods_hot', views.GoodHotSaleView.as_view()),
    url(r'^goods_recommend', views.GoodRecommendView.as_view()),
    url(r'^goods_new', views.GoodNewOnSaleView.as_view()),
    url(r'^banner_show', views.BannerList.as_view()),
    url(r'^icon_show', views.ICONQueryShow.as_view()),
    url(r'^show_icon_goods', views.GoodsAllTemplateView.as_view()),
    url(r'^block_show', views.FromBlockShow.as_view()),
    url(r'^show_block_goods', views.GoodssAllBlockView.as_view()),
    url(r'^top_search', views.SearchView.as_view()),

    # url(r'^goods_star', views.GoodStarView.as_view()),
]

router = DefaultRouter()
router.register('spus/search', views.SPUSearchViewSet, base_name='spus_search')

urlpatterns += router.urls
