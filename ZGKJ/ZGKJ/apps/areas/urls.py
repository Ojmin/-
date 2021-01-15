from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'areas', views.AreasViewset, base_name='areas')

urlpatterns = [
    url(r'^user_areas', views.UserAcceptGoodsArea.as_view()),
    url(r'^default_area', views.DefaultArea.as_view()),
    # url(r'', views.DefaultArea.as_view()),

]

urlpatterns += router.urls