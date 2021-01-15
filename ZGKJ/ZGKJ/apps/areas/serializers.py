from rest_framework import serializers

from goods.models import Area


class AreaSerializer(serializers.ModelSerializer):
    """省序列化器"""

    class Meta:
        model = Area
        fields = ['id', 'name']


class SubAreaSerializer(serializers.ModelSerializer):
    """城市和区县序列化器"""

    # 使用subs关联AreaSerializer
    # area_set = AreaSerializer(many=True, read_only=True)
    subs = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'name', 'subs']