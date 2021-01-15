from rest_framework import serializers
import re
from django_redis import get_redis_connection

from goods.models import User, SPU, Collect


class SKUSerializer(serializers.ModelSerializer):
    """用户浏览记录序列化器"""

    class Meta:
        model = SPU
        fields = ['id', 'name', 'price', 'default_image_url', 'comments']


class UserBrowsingHistorySerializer(serializers.Serializer):
    """用户浏览记录序列化器
    接受SPU_id,校验SPU_id,保存SPU_id到redis
    """
    SPU_id = serializers.IntegerField(label='商品ID', min_value=1)  # 1123456781

    def validate_SPU_id(self, value):
        """
        校验SPU_id
        :param value: SPU_id
        :return: SPU_id
        """
        try:
            SPU.objects.get(id=value)
        except SPU.DoesNotExist:
            raise serializers.ValidationError('SPU_id不存在')

        return value

    def create(self, validated_data):
        """
        重写create方法将SPU_id到redis
        :param validated_data: {'SPU_id':1}
        :return: validated_data
        """

        SPU_id = validated_data.get('SPU_id')
        user_id = self.context['request'].user.id

        # 创建连接到redis的对象
        redis_conn = get_redis_connection('history')
        pl = redis_conn.pipeline()

        # 去重
        pl.lrem('history_%s' % user_id, 0, SPU_id)
        # 添加
        pl.lpush('history_%s' % user_id, SPU_id)
        # 截取
        pl.ltrim('history_%s' % user_id, 0, 4)
        # 执行
        pl.execute()

        return validated_data

#
# class UserAddressSerializer(serializers.ModelSerializer):
#     """
#     用户地址序列化器
#     """
#     province = serializers.StringRelatedField(read_only=True)
#     city = serializers.StringRelatedField(read_only=True)
#     district = serializers.StringRelatedField(read_only=True)
#     province_id = serializers.IntegerField(label='省ID', required=True)
#     city_id = serializers.IntegerField(label='市ID', required=True)
#     district_id = serializers.IntegerField(label='区ID', required=True)
#
#     class Meta:
#         model = Address
#         # exclude 拒绝传递列表参数
#         exclude = ('user', 'is_deleted', 'create_time', 'update_time')
#
#     def validate_mobile(self, value):
#         """
#         验证手机号
#         """
#         if not re.match(r'^1[3-9]\d{9}$', value):
#             raise serializers.ValidationError('手机号格式错误')
#         return value
#
#     # 重写create方法，追加地址的外键的存储
#     def create(self, validated_data):
#         # user = validated_data['user']
#         # 读取当前经过认证和权限的登录用户
#         user = self.context['request'].user
#         validated_data['user'] = user
#
#         address = Address.objects.create(**validated_data)
#
#         return address
#
#
# class AddressTitleSerializer(serializers.ModelSerializer):
#     """
#     地址标题
#     """
#
#     class Meta:
#         model = Address
#         fields = ('title',)


class UserDetailSerializer(serializers.ModelSerializer):
    """对用户基本信息进行序列化"""

    class Meta:
        model = User
        fields = ['id', 'username', 'mobile', 'email', 'email_active']


class CollectModelSerializer(serializers.ModelSerializer):
    """
    用户收藏列表
    """

    class Meta:
        model = Collect
        fields = "__all__"
