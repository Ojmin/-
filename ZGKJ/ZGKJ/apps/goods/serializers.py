from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from .models import SPU, Banner, GoodsStyle
from goods.search_indexes import SPUIndex

class GoodsStyleSerializersModel(serializers.ModelSerializer):
    class Meta:
        model = GoodsStyle
        fields = ['price', 'qiniu_image_url']


class SPUSerializer(serializers.ModelSerializer):
    goodsStyleList = serializers.SerializerMethodField()
    def get_goodsStyleList( self, row):
        try:
            sList = GoodsStyle.objects.filter (spu_code_id=row.spu_code)
            sList = GoodsStyleSerializersModel ( sList, many=True )
            return sList.data
        except:
            return [ ]
    class Meta:
        model = SPU
        fields = "__all__"


class SPUIndexSerializer(HaystackSerializer):
    """
    SPU索引结果数据序列化器
    """
    object = SPUSerializer(read_only=True)

    class Meta:
        index_classes = [SPUIndex]
        fields = ('text', 'object')


# banner图展示
class BannerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"