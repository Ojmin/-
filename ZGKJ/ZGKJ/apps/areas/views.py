import pickle

from django.http import JsonResponse
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from goods.models import User
from goods.models import Area, UserAcceptGoodAreaModel
from . import serializers


# Create your views here.


class AreasViewset(CacheResponseMixin, ReadOnlyModelViewSet):
    """省市区三级联动数据"""

    # renderer_classes = (JSONRenderer,)
    # 指定序列化器
    # serializer_class = serializers.AreaSerializer
    # 重写父类，返回json对象
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data, safe=False)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

    def get_serializer_class(self):
        # 根据不同的行为，指定不同的序列化器
        if self.action == 'list':
            return serializers.AreaSerializer
        else:
            return serializers.SubAreaSerializer

    # 禁用分页
    pagination_class = None

    # 指定查询集
    # queryset = Area.objects.all()
    def get_queryset(self):
        # 根据不同的行为，指定不同的查询集
        if self.action == 'list':
            # 如果是list行为，表示返回订顶级数据
            # print(Area.objects.filter(parent=None),1)
            # for i in Area.objects.filter(parent=None):
            #     print(i ,end='\n')
            return Area.objects.filter(parent=None)
        else:
            # print(Area.objects.all(),2)
            return Area.objects.all()


class UserAcceptGoodsArea(APIView):
    def get(self, request):
        # user_id = request.GET['user_id']
        user = request.wx_user

        try:
            area_id = request.GET['area_id']
            user_areas = UserAcceptGoodAreaModel.objects.get(user_id=user.id, id=area_id)

        except Exception as e:

            area_id = int(user.default_area)
            print(area_id)
            user_areas = UserAcceptGoodAreaModel.objects.filter(user_id=user.id, is_deleted=False).order_by(
                '-update_time')
            area_list = [{'default_area': area_id}]
            for area in user_areas:
                data = {}
                data['area_id'] = area.id
                data['province'] = area.province
                data['city'] = area.city
                data['district'] = area.district
                data['place'] = area.place
                data['mobile'] = area.mobile
                data['AcceptPerson'] = area.AcceptPerson
                area_list.append(data)
            return Response(area_list, status=status.HTTP_200_OK)
        else:
            default_area = User.objects.get(id=user.id).default_area
            single_area = {
                'area_id': user_areas.id,
                "province": user_areas.province,
                "city": user_areas.city,
                "district": user_areas.district,
                'place': user_areas.place,
                'mobile': user_areas.mobile,
                'AcceptPerson': user_areas.AcceptPerson

            }
            if default_area == int(area_id):
                single_area['is_default_area'] = True
            else:
                single_area['is_default_area'] = False
            return Response(single_area)

    def post(self, request):
        user = request.wx_user
        user_id = user.id
        city = request.POST['city']
        province = request.POST['province']
        district = request.POST['district']
        place = request.POST['place']
        mobile = request.POST['mobile']
        AcceptPerson = request.POST['AcceptPerson']
        user_areas = UserAcceptGoodAreaModel(user_id=user_id, province=province, city=city, district=district,
                                             place=place, mobile=mobile, AcceptPerson=AcceptPerson)
        user_areas.save()
        return Response({"message": '添加地址成功'}, status=status.HTTP_200_OK)

    def put(self, request):
        # user_id = request.data['user_id']
        area_id = request.data['area_id']
        area = UserAcceptGoodAreaModel.objects.get(id=area_id)
        area.province = request.data['province']
        area.city = request.data['city']
        area.district = request.data['district']
        area.place = request.data['place']
        area.AcceptPerson = request.data['AcceptPerson']
        area.mobile = request.data['mobile']
        area.save()

        return Response({"message": '修改地址成功'}, status=status.HTTP_200_OK)

    def delete(self, request):
        area_id = request.data['area_id']
        G = UserAcceptGoodAreaModel.objects.get(id=area_id)
        G.is_deleted = True
        G.save()
        return Response({'message': '删除地址成功'}, status=status.HTTP_200_OK)


#
class DefaultArea(APIView):
    def get(self, request):
        # user_id = request.GET['user_id']
        user = request.wx_user
        area_id = int(user.default_area)
        default_area = UserAcceptGoodAreaModel.objects.get(id=area_id)
        return Response({
            'area_id': default_area.id,
            'province': default_area.province,
            'city': default_area.city,
            'district': default_area.district,
            'place': default_area.place,
            'mobile': default_area.mobile,
            'AcceptPerson': default_area.AcceptPerson,
        })

    def put(self, request):
        area_id = request.data['area_id']
        user = request.wx_user
        if int(user.default_area) == int(area_id):
            user.default_area = 0
        else:
            user.default_area = area_id
        user.save()
        # 刷新缓存

        redis_conn = get_redis_connection('mySession')
        redis_conn.set('mySession_%s' % request.wx_user.id, pickle.dumps(user), 30 * 60)
        return Response({'message': '修改默认地址成功'}, status=status.HTTP_200_OK)
