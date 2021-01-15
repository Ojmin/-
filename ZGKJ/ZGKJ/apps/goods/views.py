
import datetime
import logging
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from goods.serializers import SPUIndexSerializer, BannerModelSerializer
from goods.models import User, GoodsStock, GoodsCate, SPU, \
                        GoodsStyle, Collect, GoodsNumbers, \
                        Banner, LayouTemplate, GoodsLayouTemplate, \
                        FromBlock, FromGoods, TopSearch, FreightManage, \
                        CityPostage
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.response import Response
import json
from django.shortcuts import render
from django.core.paginator import Paginator  # 导入模块
from ZGKJ.settings.dev import QINIU_ACCESS_KEY, QINIU_SECRET_KEY
from qiniu import Auth, etag, put_data
logger = logging.getLogger('django')
spu_list = ["SPU202010009","SPU202010030","SPU202010031","SPU202010025","SPU202010018","SPU202010026","SPU202010022","SPU202010001","SPU202010021"]

# Create your views here.

class GoodsDetail(APIView):
    def get(self, request):
        return render(request, 'goods/index.html')


# 详情页的查

class SPUView(APIView):
    def get(self, request):
        mes =dict()
        try:
            spu_code = request.GET['spu_code']
        except Exception as e:
            return Response({'msg': 'no spu_code','code':status.HTTP_400_BAD_REQUEST})
        try:
            user_id = int(request.META.get('HTTP_USERID'))
        # 没有user_id
        except:
            try:
                G = SPU.objects.get(spu_code=spu_code)
            except Exception as e:
                print(e)
                return Response('没有查到该货号的商品', status=status.HTTP_400_BAD_REQUEST)
            # 取出 库存 和 数量 列表
            # numbers = GoodsStyle.objects.filter(spu_code_id=G.spu_code).values('goodsNumber')
            # for number in numbers:
            #     size_stock_list = GoodsNumbers.objects.filter(
            #     goodsNumber=G.goodsstyle_set.filter(spu_code_id=G)
            # ).all()
            # 取出 货号 列表
            styles = GoodsStyle.objects.filter(spu_code=spu_code).all()
            goodsStyleList = list()
            for style in styles:
                styledict = dict ()
                styledict['goodsNumber'] = style.goodsNumber
                styledict['price'] = style.price
                styledict['qiniu_image_url'] = style.qiniu_image_url
                styledict['default_image_url'] = style.default_image_url
                styledict['goods_color'] = style.goods_color
                styledict['model3D'] = style.model3D
                styledict['modelPoints'] = style.modelPoints
                size_stock_list = GoodsNumbers.objects.filter (goodsNumber=style.goodsNumber).all()
                goodsSize = [ ]
                for i in size_stock_list:
                    dicts = dict ()
                    dicts[ 'goods_size' ] = i.goods_size
                    dicts[ 'goods_count' ] = i.goods_count
                    goodsSize.append ( dicts )
                styledict[ 'size_stock' ] = goodsSize
                goodsStyleList.append(styledict)
            mes['name'] = G.name
            mes['spu_code'] = G.spu_code
            mes[ 'base' ] = G.base
            mes[ 'goods_size' ] = G.size
            mes[ 'brandStory' ] = G.brandStory
            mes[ 'subTitle' ] = G.subTitle
            mes[ 'details' ] = G.details
            mes[ 'OnSaleDay' ] = G.OnSaleDay
            mes[ 'sales' ] = G.sales
            mes[ 'cate' ] = G.cate.name
            mes[ 'brand' ] = G.brand.name
            mes[ 'sizeImage' ] = G.brand.sizeImage
            mes[ 'star' ] = 0
            manage = FreightManage.objects.get ( id=int ( G.moXing ) )
            mes['include_section'] = manage.include_section
            mes['moXing'] = manage.tname
            mes['freight_status'] = manage.freight_status
            mes['initial_money'] = manage.initial_money
            mes['default_section'] = manage.default_section
            mes['more_money'] = manage.more_money
            city = CityPostage.objects.filter ( freight=manage.id )
            print(city)
            citypostageList = list()
            for i in city:
                cdict = dict()
                cdict['id'] = i.id
                cdict['include_section'] = i.area
                cdict['initial_money'] = i.initial_money
                cdict['more_money'] = i.more_money
                citypostageList.append(cdict)
            mes['citypostageList'] =citypostageList
            mes[ 'goodsStyleList' ] = goodsStyleList

        #有user_id
        else:
            collect = Collect.objects.filter(user_id=user_id).all()
            collectList = list()
            for coll in collect:
                collectList.append(coll.spu_id)
            G = SPU.objects.get ( spu_code=spu_code )
            if G.id in collectList:
                star = 1
            else:
                star = 0
            try:
                G = SPU.objects.get(spu_code=spu_code)
            except Exception as e:
                print(e)
                return Response('没有查到该货号的商品', status=status.HTTP_400_BAD_REQUEST)
            # # 取出 库存 和 数量 列表
            # size_stock_list = GoodsStock.objects.filter(
            #     goodsNumber=G.goodsstyle_set.filter(spu_code=G.spu_code)[0].goodsNumber
            # ).all()
            # 取出 货号 列表
            styles = GoodsStyle.objects.filter(spu_code=spu_code).all()
            goodsStyleList = list()
            for style in styles:
                styledict = dict()
                styledict['goodsNumber'] = style.goodsNumber
                styledict['price'] = style.price
                styledict['qiniu_image_url'] = style.qiniu_image_url
                styledict['default_image_url'] = style.default_image_url
                styledict['goods_color'] = style.goods_color
                styledict['model3D'] = style.model3D
                styledict['modelPoints'] = style.modelPoints
                goodsSize = [ ]
                size_stock_list = GoodsNumbers.objects.filter ( goodsNumber=style.goodsNumber ).all ()
                for i in size_stock_list:
                    dicts = dict ()
                    dicts[ 'goods_size' ] = i.goods_size
                    dicts[ 'goods_count' ] = i.goods_count
                    goodsSize.append ( dicts )
                styledict[ 'size_stock' ] = goodsSize
                goodsStyleList.append(styledict)
            mes['name'] = G.name
            mes['spu_code'] = G.spu_code
            mes['moXing'] = G.moXing
            mes['base'] = G.base
            mes['goods_size'] = G.size
            mes['brandStory'] = G.brandStory
            mes['subTitle'] = G.subTitle
            mes['details'] = G.details
            mes['OnSaleDay'] = G.OnSaleDay
            mes['sales'] = G.sales
            mes['cate'] = G.cate.name
            mes['brand'] = G.brand.name
            mes['sizeImage'] = G.brand.sizeImage
            mes['star'] = star
            manage = FreightManage.objects.get ( id=int ( G.moXing ) )
            mes[ 'moXing' ] = manage.tname
            mes['include_section'] = manage.include_section
            mes[ 'freight_status' ] = manage.freight_status
            mes[ 'initial_money' ] = manage.initial_money
            mes[ 'default_section' ] = manage.default_section
            mes[ 'more_money' ] = manage.more_money
            city = CityPostage.objects.filter ( freight=manage.id )
            citypostageList = list ()
            for i in city:
                cdict = dict ()
                cdict[ 'id' ] = i.id
                cdict[ 'include_section' ] = i.area
                cdict[ 'initial_money' ] = i.initial_money
                cdict[ 'more_money' ] = i.more_money
                citypostageList.append ( cdict )
            mes[ 'citypostageList' ] = citypostageList
            mes['goodsStyleList'] = goodsStyleList
        return Response(mes)


# 分类
class CategoryView(APIView):
    """分类"""

    def get(self, request):
        G = GoodsCate.objects.all()
        data = {}
        for i in G:
            data[i.id] = i.name
        return Response(json.dumps(data))


class GoodsPointView(APIView):
    """添加触点"""

    def post(self, request):
        point = request.POST['data']
        goodsNumber = request.POST['goodsNumber']
        good = SPU.objects.get(goodsNumber=goodsNumber)
        good.modelPoints = point
        good.save()
        return Response({"msg": '添加触点成功'}, status=status.HTTP_200_OK)


class QiniuUpload(APIView):
    @staticmethod
    def upload(name):
        # 需要填写你的 Access Key 和 Secret Key

        # 构建鉴权对象
        q = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)

        # 要上传的空间
        bucket_name = 'zgkj1'

        # 上传后保存的文件名
        key = name

        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)

        # 要上传文件的本地路径
        return token

    def post(self, request):
        try:
            name = request.POST['name']
        except:
            return Response({"msg": "no name", 'code': -1})

        else:
            token = self.upload(name)

            return Response({"token": token, 'msg': "success"})


# 列表 带分页
class GoodsListView(APIView):
    def get(self, request):
        current_pagnum = request.GET.get('page')
        good_list = SPU.objects.all().order_by('id')
        paginator = Paginator(good_list, 10)  # 每页显示几个
        posts = paginator.page(number=int(current_pagnum))  # 这个num就是现实当前第几页
        num_pages = paginator.num_pages  # 总页数
        goodList = [{'num_pages': num_pages}]
        for i in posts:
            data = {}
            data['name'] = i.name
            data['goodsNumber'] = i.goodsNumber
            data['subTitle'] = i.subTitle
            data['default_image_url'] = str(i.default_image_url)
            data['price'] = str(i.price)
            data['sales'] = i.sales
            data['brand'] = i.brand.name
            if (datetime.datetime.now() - i.create_time.replace(tzinfo=None)).days < 7:

                data['new_good'] = 1
            else:
                data['new_good'] = 0
            if i.sales > 100:
                data['hot_sale'] = 1
            else:
                data['hot_sale'] = 0
            goodList.append(data)
        return Response(goodList)


# 推荐
class GoodRecommendView(APIView):
    '''

    '''
    def get(self, request):
        try:
            goods = SPU.objects.filter(status=True).all()
        except Exception as e:
            logger.error(e)
            return Response({'error_msg': '推荐商品不存在', 'code':status.HTTP_400_BAD_REQUEST})
        # user = request.wx_user
        goodList = [ ]
        for i in goods:
            print ( i.spu_code )
            data = {}
            data[ 'name' ] = i.name
            styles = GoodsStyle.objects.filter ( spu_code_id=i.spu_code ).all ()
            print ( styles )
            goodsStyleList = list ()
            for style in styles:
                styledict = dict ()
                styledict[ 'goodsNumber' ] = style.goodsNumber
                styledict[ 'qiniu_image_url' ] = style.qiniu_image_url
                styledict[ 'price' ] = style.price
                goodsStyleList.append ( styledict )
            data[ 'subTitle' ] = i.subTitle
            data[ 'sales' ] = i.sales
            data[ 'brand' ] = i.brand.name
            data[ 'goodsStyleList' ] = goodsStyleList
            goodList.append ( data )
        array = []
        for posts in goods:
            data = {
                'name': posts.name,
                'goodsNumber': posts.goodsNumber,
                'subTitle': posts.subTitle,
                'default_image_url': str(posts.default_image_url),
                'sales': posts.sales,
                'price': str(posts.price),
                'brand': posts.brand.name,
                "banner": str(posts.banner)
            }
            array.append(data)
        return Response(array)


# 首页一排一
class GoodHotSaleView(APIView):
    def get(self, request):
        mes = dict ()
        try:
            current_pagnum = request.GET.get ( 'p', 1 )
            spu = SPU.objects.filter ( goodsnews__type=2 ,status=True).all ().order_by ( 'goodsnews__sort' )
            paginator = Paginator ( spu, 10 )  # 每页显示几个
            posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
            num_pages = paginator.num_pages  # 总页数
            spuList = list ()
            for i in posts:  # 获取当前页的数据进行封装
                data = {}
                data[ 'name' ] = i.name
                styles = GoodsStyle.objects.filter ( spu_code_id=i.spu_code ).all ().order_by('price')
                goodsStyleList = list ()
                for style in styles:
                    styledict = dict ()
                    styledict[ 'goodsNumber' ] = style.goodsNumber
                    styledict[ 'qiniu_image_url' ] = style.qiniu_image_url
                    styledict[ 'price' ] = style.price
                    goodsStyleList.append ( styledict )
                data[ 'subTitle' ] = i.subTitle
                data[ 'sales' ] = i.sales
                if i.spu_code in spu_list:
                    data['AR_STATUS'] = 1
                else:
                    data['AR_STATUS'] = 0
                data[ 'spu_code' ] = i.spu_code
                data[ 'brand' ] = i.brand.name
                data[ 'goodsStyleList' ] = goodsStyleList
                spuList.append ( data )
                mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'goodList' ] = spuList
            mes[ 'tpage' ] = num_pages
            mes[ 'message' ] = 'The query is succssful'
        except:
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'goodList' ] = [ ]
            mes[ 'message' ] = 'databases Empty data '
        return Response ( mes )

# Banner 图展示
class BannerList(APIView):
    def get( self, request):
        # Statically initializes the dictionary
        mes = dict()
        # Query the data in the table
        banner = Banner.objects.filter(is_start=True).all().order_by('sort')
        # erialize the data and pass it to the front end
        data = BannerModelSerializer(banner, many=True)
        mes[ 'bannerList' ] = data.data
        mes['code'] = status.HTTP_200_OK
        mes['message'] = 'The query is succssful'
        # id = request.wx_user.id
        return Response(mes)


# 新品上市
class GoodNewOnSaleView(APIView):
    def get(self, request):
        mes = dict ()
        try:
            posts = SPU.objects.filter(goodsnews__type=1).all().order_by('goodsnews__sort') #[:10]
            goodList = []
            for i in posts:
                data = {}
                data['name'] = i.name
                styles = GoodsStyle.objects.filter(spu_code_id=i.spu_code).all()
                goodsStyleList = list()
                for style in styles:
                    styledict = dict()
                    styledict['goodsNumber'] = style.goodsNumber
                    styledict['qiniu_image_url'] = style.qiniu_image_url
                    styledict['price'] = style.price
                    goodsStyleList.append(styledict)
                data['subTitle'] = i.subTitle
                data['spu_code'] = i.spu_code
                data['sales'] = i.sales
                data['brand'] = i.brand.name
                data['goodsStyleList'] = goodsStyleList
                goodList.append(data)
                mes['code'] = status.HTTP_200_OK
                mes['goodList'] = goodList
                mes['message'] = 'The query is succssful'
        except:
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'goodList' ] = []
            mes[ 'message' ] = 'databases Empty data '
        return Response(mes)


# ICON 查询
class ICONQueryShow ( APIView ):
    '''
    :param
    :type
    :return
    '''
    def get ( self, request ):
        # 获取 ICON 布局下的 产品信息
        mes = dict ()
        try:
            temp = LayouTemplate.objects.filter ( is_start=True ).values ( 'id', 'name', 'image_url' ).order_by('sort')
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'ICONList' ] = temp
            mes[ 'message' ] = 'The query is succssful'
        except:
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'ICONList' ] = []
            mes[ 'message' ] = 'Lack of data in database'
        return Response ( mes )


# query icon不同类下面的产品
class GoodsAllTemplateView(APIView):
    def get( self, requset):
        # 获取icon id
        id = requset.GET.get('id')
        current_pagnum = requset.GET.get ( 'p', 1)
        # 查询 id 下的数据
        queryGoods = GoodsLayouTemplate.objects.filter ( temp_id= id ,spu_code__status=True ).all ()
        paginator = Paginator ( queryGoods, 10 )  # 每页显示几个
        posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
        num_pages = paginator.num_pages  # 总页数
        # 遍历 QuerySet 封装数据
        goodsList = list()
        for goods in posts:
            goodsdict = dict()
            goodsdict[ 'id' ] = goods.id
            goodsdict['temp_id'] = goods.temp_id
            goodsdict['spu_code'] = goods.spu_code_id
            if goods.spu_code_id in spu_list:
                goodsdict['AR_STATUS'] = 1
            else:
                goodsdict['AR_STATUS'] = 0
            goodsdict[ 'goods_name' ] = goods.spu_code.name
            goodsdict[ 'sales' ] = (goods.spu_code.sales + goods.spu_code.base)
            goodsdict[ 'details' ] = goods.spu_code.details
            goodsdict[ 'subTitle' ] = goods.spu_code.subTitle
            number = GoodsStyle.objects.filter(spu_code_id=goods.spu_code).\
            values('qiniu_image_url', 'price', 'goodsNumber')
            goodsdict[ 'goodsNumberList' ] = number
            goodsList.append(goodsdict)
        mes = dict ()
        mes[ 'tpage' ] = num_pages
        mes[ 'code' ] = status.HTTP_200_OK
        mes[ 'message' ] = 'The query is succssful'
        mes[ 'IconGoodsList' ] = goodsList
        return Response(mes)



# FROM Block 查询
class FromBlockShow ( APIView ):
    def get ( self, request ):
        # 获取 Block 布局下的 产品信息
        mes = dict ()
        try:
            block = FromBlock.objects.filter ( is_start=True ).values ( 'id', 'name').order_by('sort')
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'BlockList' ] = block
            mes[ 'message' ] = 'The query is succssful'
        except:
            mes[ 'code' ] = status.HTTP_200_OK
            mes[ 'BlockList' ] = []
            mes[ 'message' ] = 'Lack of data in database'
        return Response ( mes )


# query block不同类下面的产品
class GoodssAllBlockView(APIView):
    def get( self, requset):
        # 获取icon id
        id = requset.GET.get('id')
        current_pagnum = requset.GET.get ( 'p', 1 )
        # 查询 id 下的数据
        queryGoods = FromGoods.objects.filter ( block_id=id, spu_code__status=True ).all ().order_by ( 'sort' )
        paginator = Paginator ( queryGoods, 10 )  # 每页显示几个
        posts = paginator.page ( number=int ( current_pagnum ) )  # 这个num就是现实当前第几页
        num_pages = paginator.num_pages  # 总页数
        # 查询 id 下的数据
        # 遍历 QuerySet 封装数据
        goodsList = list()
        for goods in posts:
            goodsdict = dict()
            goodsdict['block_id'] = goods.block_id
            goodsdict[ 'id' ] = goods.id
            goodsdict['spu_code'] = goods.spu_code_id
            goodsdict[ 'goods_name' ] = goods.spu_code.name
            goodsdict[ 'sales' ] = goods.spu_code.sales +goods.spu_code.base
            goodsdict[ 'details' ] = goods.spu_code.details
            goodsdict[ 'subTitle' ] = goods.spu_code.subTitle
            number = GoodsStyle.objects.filter(spu_code_id=goods.spu_code).\
            values('qiniu_image_url', 'price', 'goodsNumber')
            goodsdict[ 'goodsNumberList' ] = number
            goodsList.append(goodsdict)
        mes = dict ()
        mes[ 'code' ] = status.HTTP_200_OK
        mes[ 'goodsList' ] = goodsList
        mes[ 'tpage' ] = num_pages
        mes[ 'message' ] = 'The query is succssful'
        return Response(mes)


class SearchView(APIView):
    '''
    获取搜词入库
    '''
    def post( self, request):
        #获取搜索词
        mes = dict()
        import time
        try:
            text = request.POST.get ( 'text' ).strip ()
        except:
            text = None
        if text !=None:
            try:
                search = TopSearch.objects.filter(search_name=text).order_by('-serach_time')[0]
                # 判断上一次时间 是否和当天时间是同一天
                if ("%s-%.2d-%.2d" % (search.serach_time.year, search.serach_time.month, search.serach_time.day))\
                        .strip() == str(time.strftime('%Y-%m-%d ',time.localtime(time.time()))).strip(): #%H:%M:%S 时分秒
                    search.search_count +=1
                    search.save()
                    mes[ 'code' ] = status.HTTP_200_OK
                    mes[ 'message' ] = 'search add succssful'
                else:
                    S = TopSearch.objects.create(search_name=text,
                                                 search_count=1,
                                                 )
                    S.save()
                    mes[ 'code' ] = status.HTTP_200_OK
                    mes[ 'message' ] = 'add succssful'
            except:
                S = TopSearch.objects.create ( search_name=text, search_count=1,
                                                )
                S.save ()
                mes[ 'code' ] = status.HTTP_200_OK
                mes[ 'message' ] = 'add succssful'
        else:
            mes[ 'code' ] = status.HTTP_400_BAD_REQUEST
            mes[ 'message' ] = 'data missing'
        return Response(mes)

    def get( self, request):
        search= TopSearch.objects.all().order_by('-search_count')[:10]
        searchList = list()
        for i in search:
            data = dict()
            data['search_name']=i.search_name
            searchList.append(data)
        mes = dict()
        mes['searchList'] = searchList
        mes[ 'code' ] = status.HTTP_200_OK
        mes[ 'message' ] = 'The query is succssful'
        return Response(mes)
# 搜索
class SPUSearchViewSet(HaystackViewSet):
    """
    SKU搜索

    """

    # 返回json重写父类
    def options(self, request, *args, **kwargs):
        """
        Handler method for HTTP 'OPTIONS' request.
        """
        if self.metadata_class is None:
            return self.http_method_not_allowed(request, *args, **kwargs)
        data = self.metadata_class().determine_metadata(request, self)
        return JsonResponse(data, status=status.HTTP_200_OK)

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

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return JsonResponse(self.paginator.get_paginated_response(data, safe=False))

    # 禁用分页
    pagination_class = None

    index_models = [SPU]

    serializer_class = SPUIndexSerializer


