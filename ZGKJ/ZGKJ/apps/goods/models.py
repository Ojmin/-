from django.db import models
from ZGKJ.utils.models import BaseModel
from django.utils.safestring import mark_safe

'''
python manage.py makemgrations
python manage.py mgrate
'''

"""
使用 python manage.py inspectdb > apps/models.py
反向生成的模型
"""


class RefundOrder ( BaseModel ):
    """退货订单表"""
    ORDER_STATUS_CHOICES = (
        (1, "审核中"),
        (2, "待买家发货"),
        (3, "待卖家收货"),
        (4, "待退款"),
        (5, "已完成"),
        (6, "已取消"),
        (7, "审核不通过"),
    )
    ORDER_TYPE = (
        (1, '退货退款'),
        (2, '仅退款'),

    )
    user_id = models.IntegerField ( verbose_name="用户id" )
    out_refund_no = models.CharField ( max_length=64, verbose_name="退货订单号" )
    order_sn = models.CharField ( max_length=64, verbose_name="订单号" )
    order_amount = models.DecimalField ( decimal_places=2, max_digits=10, verbose_name="订单金额" )
    refund_amount = models.DecimalField ( decimal_places=2, max_digits=10, verbose_name="退款金额" )
    is_refund = models.BooleanField ( default=False, verbose_name="是否已退款" )
    status = models.SmallIntegerField ( choices=ORDER_STATUS_CHOICES, verbose_name="退款订单状态" )
    not_pass_reason = models.CharField ( max_length=200, verbose_name="审核不通过原因", blank=True, null=True )
    refund_reason = models.CharField ( max_length=255, verbose_name="退款原因", blank=True, null=True )
    is_delete = models.BooleanField ( default=False )
    re_type = models.SmallIntegerField ( choices=ORDER_TYPE, verbose_name="退货类型" )
    logistics_no = models.CharField ( max_length=64, verbose_name="运单号", blank=True, null=True )
    logistics_company = models.SmallIntegerField ( verbose_name="物流公司id", blank=True, null=True )
    user_info = models.CharField ( max_length=70, default='', verbose_name='买家信息' )
    goods_name = models.CharField ( max_length=35, default='', verbose_name='商品名称' )
    goodsNumber = models.CharField ( max_length=64, default='', verbose_name='货号' )
    goods_spu = models.CharField ( max_length=70, default='', verbose_name='商品spu编码' )

    class Meta:
        db_table = 't_refund'
        verbose_name = '退款表'
        verbose_name_plural = verbose_name

    def __str__ ( self ):
        return "{}退款{}".format ( self.order_sn, self.refund_amount )

    # 验证是否已经退款
    def save ( self, *args, **kwargs ):
        if self.is_refund:
            return "{}已经退过款了！".format ( self.order_sn )

        super ( RefundOrder, self ).save ( *args, **kwargs )  # Call the "real" save() method.


# 商品库存表
class GoodsStock ( BaseModel ):
    size = models.CharField ( default='', max_length=8, verbose_name='尺码' )
    stock = models.IntegerField ( default=0, verbose_name='总库存' )
    goodsNumber = models.CharField ( default=' ', max_length=40, verbose_name='货号' )

    class Meta:
        db_table = 'tb_goods_stock'
        verbose_name = '商品库存'


class Area ( models.Model ):
    """
    行政区划
    """
    name = models.CharField ( max_length=20, verbose_name='名称' )
    parent = models.ForeignKey ( 'self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True,
                                 verbose_name='上级行政区划' )

    # 如果不自定义关联字段 related_name='subs',
    # 那么默认的关联字段就是 area_set

    class Meta:
        db_table = 'tb_areas'
        verbose_name = '行政区划'
        verbose_name_plural = '行政区划'

    def __str__ ( self ):
        return self.name


class Brand ( BaseModel ):
    """
    品牌
    """
    name = models.CharField ( max_length=20, verbose_name='名称' )
    logo = models.CharField ( max_length=200, verbose_name='Logo图片' )
    sizeImage = models.CharField ( max_length=200, default='', verbose_name='品牌尺码图片(非必传)' )

    class Meta:
        db_table = 'tb_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__ ( self ):
        return self.name


# 用户收货地址表
class UserAcceptGoodAreaModel ( BaseModel ):
    user_id = models.IntegerField ( verbose_name='用户id' )
    AcceptPerson = models.CharField ( max_length=10, verbose_name='收货人' )
    province = models.CharField ( max_length=10, verbose_name='省' )
    city = models.CharField ( max_length=10, verbose_name='市' )
    district = models.CharField ( max_length=10, verbose_name='区' )
    place = models.CharField ( max_length=50, verbose_name='地址' )
    mobile = models.CharField ( max_length=11, verbose_name='手机' )
    is_deleted = models.BooleanField ( default=False, verbose_name='逻辑删除' )

    class Meta:
        db_table = 'tb_user_good_areas'
        verbose_name = '用户收货地址'
        verbose_name_plural = '该用户的收货地址'

    def __str__ ( self ):
        return self.user_id + '：添加地址成功'


# 商品分类guige表
class GoodsCate ( BaseModel ):
    name = models.CharField ( max_length=10, unique=True, verbose_name='分类名称' )
    SPEC = models.CharField ( max_length=50, verbose_name=' 规格大小' )

    class Meta:
        db_table = 'tb_goods_cate'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


#
class OrderInfo ( BaseModel ):
    """
    订单信息
    """

    ORDER_STATUS_ENUM = {
        "UNPAID": 1,
        "UNSEND": 2,
        "UNRECEIVED": 3,
        "FINISHED": 4,
    }

    ORDER_STATUS_CHOICES = (
        (1, "待支付"),
        (2, "待发货"),
        (3, "已发货"),
        (4, "待收货"),
        (5, "已完成"),
        (6, "已取消"),
        (7, "退款中"),
        (8, "已退款"),
        (9, "退款失败")
    )

    # 1.23   float 1.2299999999
    # 1.23   Decimal   1   23     1.23
    order_sn = models.CharField ( unique=True, db_index=True, max_length=64, verbose_name="订单号" )
    actual_payment = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='实际支付' )
    image = models.CharField ( default='', max_length=200, verbose_name='图片路径' )
    payment_time = models.DateTimeField ( auto_now_add=True, verbose_name='支付时间' )
    status = models.SmallIntegerField ( choices=ORDER_STATUS_CHOICES, default=1, verbose_name="订单状态" )
    goods_name = models.CharField ( max_length=35, verbose_name='商品名称' )
    total_count = models.IntegerField ( default=1, verbose_name="商品总数" )
    goods_color = models.CharField ( max_length=8, verbose_name='商品颜色' )
    price = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='单价' )
    total_amount = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name="商品总金额" )
    goodsNumber = models.CharField ( max_length=64, db_index=True, verbose_name='货号' )
    goods_spu = models.CharField ( max_length=70, default='', verbose_name='商品spu编码' )
    address = models.ForeignKey ( UserAcceptGoodAreaModel, on_delete=models.PROTECT, verbose_name="收获地址" )
    user_info = models.CharField ( max_length=70, verbose_name='买家信息' )
    size = models.CharField ( max_length=5, verbose_name='尺码' )
    user_id = models.IntegerField ( verbose_name="下单用户ID" )
    wuliu_info = models.CharField ( default='', max_length=60, verbose_name='物流信息(公司,单号)' )
    freight = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name="运费" )
    is_deleted = models.BooleanField ( default=False, verbose_name='逻辑删除' )
    # 为提现加
    user_nickname = models.CharField ( max_length=32, verbose_name="用户昵称" )
    invite_user_id = models.IntegerField ( verbose_name="邀请人id" )
    invite_nickname = models.CharField ( max_length=32, verbose_name="邀请人昵称" )
    reason = models.CharField ( max_length=200, default='', blank=True, verbose_name='取消订单原因' )

    class Meta:
        db_table = "tb_order_info"
        verbose_name = '订单基本信息'
        verbose_name_plural = verbose_name


# 商品的spu表
class SPU ( BaseModel ):
    """
    商品SPU  款式具体的规格
    """
    # _user = models.ForeignKey('User', on_delete=models.CASCADE, editable=False, null=True)  # 创建该数据的登录用
    cate = models.ForeignKey ( GoodsCate, on_delete=models.PROTECT, verbose_name='从属类别' )
    name = models.CharField ( max_length=50, verbose_name='名称' )
    brand = models.ForeignKey ( Brand, on_delete=models.CASCADE, verbose_name='品牌' )
    subTitle = models.TextField ( max_length=150, verbose_name='副标题' )
    brandStory = models.TextField ( default='', max_length=2000, verbose_name='品牌故事', blank=True, null=True )
    status = models.BooleanField ( default=False, verbose_name='商品上架状态' )
    details = models.TextField ( default='', verbose_name='详情', blank=True, null=True )
    OnSaleDay = models.CharField ( max_length=30, verbose_name='发售日期' )
    moXing = models.CharField ( max_length=50, verbose_name='模型地址(非必填)', blank=True, null=True )
    sales = models.IntegerField ( default=0, verbose_name='销量' )
    spu_code = models.CharField ( db_index=True, max_length=50, default='', unique=True, verbose_name='商品的spu码' )
    base = models.IntegerField ( default=0, verbose_name='商品基数' )
    size = models.CharField ( default='', max_length=40, verbose_name='商品尺码', blank=False )

    class Meta:
        db_table = 'tb_spu'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__ ( self ):
        return '%s: %s' % (self.id, self.name)


# 商品货号表
class GoodsStyle ( BaseModel ):
    # 鞋子，服装
    modelPoints = models.TextField ( default='', verbose_name='模型点', blank=True, null=True )
    # 逗号分隔，去七牛云拿
    default_image_url = models.CharField ( default='', max_length=80, verbose_name='默认图片', blank=True, null=True )
    qiniu_image_url = models.CharField ( default='', max_length=200, verbose_name='七牛云的图片链接(非必填)', blank=True,
                                         null=True )
    goodsNumber = models.CharField ( db_index=True, unique=True, max_length=30, verbose_name='货号' )
    model3D = models.CharField ( default='', max_length=100, verbose_name="上传模型", blank=True, null=True )
    price = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='单价' )
    goods_color = models.CharField ( max_length=8, default='', verbose_name='商品颜色' )
    spu_code = models.ForeignKey ( SPU, on_delete=models.CASCADE, to_field='spu_code', verbose_name='spu编码外键' )

    class Meta:
        db_table = 'tb_goods_style'
        verbose_name = '商品货号表'

    def go_to ( self ):
        goodsNumber = self.goodsNumber
        # from django.utils.safestring import mark_safe  #将字符串返回为安全的HTML标签类型
        return mark_safe (
            '<a href="http://zugou.vip/html/goods/manage-shoe-detail.html?goodsNumber={}" target="_blank">添加触点</a>'.format (
                goodsNumber ) )

    go_to.short_description = '添加触点'


# 商品数量表
class GoodsNumbers ( BaseModel ):
    goods_num = models.IntegerField ( default=0, verbose_name='总采购数量' )
    goods_sales = models.IntegerField ( default=0, verbose_name='销售量' )
    goods_count = models.IntegerField ( default=0, verbose_name='剩余商品数量(采购量-销售量)' )
    goodsNumber = models.ForeignKey ( GoodsStyle, on_delete=models.CASCADE, to_field='goodsNumber',
                                      verbose_name='外键字段对应货号' )
    goods_size = models.CharField ( max_length=20, verbose_name='商品规格' )
    sole = models.CharField ( max_length=50, verbose_name='唯一串和商品数量表相同' )

    class Meta:
        db_table = 'tb_goods_size'
        verbose_name = '商品数量表'


class User ( BaseModel ):
    """自定义用户模型类"""
    nickName = models.CharField ( max_length=200, verbose_name='微信昵称' )
    gender = models.IntegerField ( default=1, verbose_name='性别' )  # 1男2女
    language = models.CharField ( max_length=10, verbose_name='语言' )
    wx_city = models.CharField ( max_length=50, verbose_name='城市' )
    wx_province = models.CharField ( max_length=50, verbose_name='省' )
    wx_country = models.CharField ( max_length=50, verbose_name='国家' )
    avatarUrl = models.CharField ( max_length=200, verbose_name='头像url' )
    commentary = models.CharField ( max_length=50, verbose_name='备注', default='', blank=True )
    openId = models.CharField ( unique=True, max_length=30, verbose_name='小程序用户openid' )
    # 默认地址
    default_area = models.IntegerField ( default=0, blank=True, verbose_name='默认收货地址' )
    # 指定用调销量基数
    ZGVIP_code = models.CharField ( max_length=30, unique=True, verbose_name='vip编码' )
    raise_base = models.IntegerField ( default=0, verbose_name='上调销售数量' )
    # 邀请码
    invitationCode = models.CharField ( default='', max_length=16, verbose_name='邀请码' )
    invite_user_id = models.IntegerField ( default=0, verbose_name="邀请人ID" )
    invite_nickname = models.CharField ( default='', max_length=100, verbose_name="邀请人昵称" )
    onroad = models.DecimalField ( default=0.00, decimal_places=2, max_digits=10, verbose_name="在途货款" )
    balance = models.DecimalField ( default=0.00, decimal_places=2, max_digits=10, verbose_name="余额" )
    invite_count = models.IntegerField ( default=0, verbose_name='成功邀请的件数' )

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 用户级别关系表
class USerDetailRank ( BaseModel ):
    top_id = models.IntegerField ( default=0, verbose_name='上上级用户ID' )
    top_code = models.CharField ( default='', max_length=7, verbose_name='上上级用户邀请码' )
    pid = models.IntegerField ( default=0, verbose_name='上级用户ID' )
    pid_code = models.CharField ( default="", max_length=7, verbose_name='上级用户邀请码' )
    type_id = models.IntegerField ( default=0, verbose_name='受邀请人id' )

    class Meta:
        db_table = 'tb_user_rank'
        verbose_name = '用户级别关系表'
        verbose_name_plural = verbose_name


# 提现明细表
class Extract ( models.Model ):
    user = models.ForeignKey ( User, on_delete=models.CASCADE, verbose_name='用户外键' )
    exract_sn = models.CharField ( max_length=50, default='', verbose_name='提现单号' )
    wx_username = models.CharField ( default='', max_length=80, verbose_name='提现微信名称' )
    extract_money = models.DecimalField ( default=0, max_digits=9, decimal_places=2, verbose_name='提现金额' )
    exract_time = models.DateTimeField ( auto_now_add=True, verbose_name='提现时间' )
    EXTRACT_STATUS = (
        (1, '未到账'),
        (2, '已到账'),
        (3, '退款失败'),
    )
    status = models.SmallIntegerField ( choices=EXTRACT_STATUS, default=1, verbose_name='提现状态' )

    class Meta:
        db_table = 'tb_extract'
        verbose_name = '提现明细表'
        verbose_name_plural = verbose_name


# 佣金明细表
class Commission ( BaseModel ):
    COMMISSION_STATUS = (
        (1, '正在途中'),
        (2, '已到账'),

    )
    order_num = models.CharField ( db_index=True, max_length=50, verbose_name='订单编号' )
    buyer_wx_name = models.CharField ( max_length=20, default='', verbose_name='买家微信' )
    buyer = models.CharField ( max_length=30, verbose_name='买家足购id', default='' )
    actual_payment = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='实际支付价格' )
    goods_name = models.CharField ( max_length=42, default='', verbose_name='商品名称' )
    payment_time = models.DateTimeField ( verbose_name='支付时间' )
    commission_status = models.SmallIntegerField ( choices=COMMISSION_STATUS, default=1, verbose_name='佣金状态' )
    up_beneficimary = models.CharField ( max_length=200, default='', verbose_name='上级收益人' )
    up_wx_user_id = models.IntegerField ( default=0, verbose_name='上级收益人足购id' )
    up_gain_money = models.DecimalField ( max_digits=7, decimal_places=2, default=0, verbose_name='上级提成' )
    # 超级管理员表
    up_up_beneficimary = models.CharField ( max_length=200, default='', verbose_name='上上级收益人' )
    up_up_wx_user_id = models.IntegerField ( default=0, verbose_name='上上级收益人足购id' )
    up_up_gain = models.DecimalField ( max_digits=7, decimal_places=2, default=0, verbose_name='上上级收益佣金' )

    class Meta:
        db_table = 'tb_commission'
        verbose_name = '佣金详情表'
        verbose_name_plural = verbose_name


# 特约二级商户
class Merchant ( BaseModel ):
    wx_code = models.CharField ( max_length=20, verbose_name='邀请码' )
    wx_id = models.CharField ( max_length=40, verbose_name='微信账号' )
    wx_name = models.CharField ( max_length=35, verbose_name='微信名称' )
    gain_section = models.CharField ( max_length=5, verbose_name='利润区间百分比' )
    commentary = models.CharField ( max_length=50, verbose_name='备注', default='', blank=True )

    class Meta:
        db_table = 'tb_merchant'
        verbose_name = '特约商户表'
        verbose_name_plural = verbose_name


# 阶梯表
class Ladder ( BaseModel ):
    ladder_section = models.CharField ( unique=True, max_length=10, verbose_name='阶梯区间(0~9,)' )

    class Meta:
        db_table = 'tb_ladder'


# 级别分销利润表
class RankSell ( BaseModel ):
    rank = models.CharField ( max_length=10, default='', verbose_name='级别' )
    gain = models.CharField ( max_length=10, default='', verbose_name='分销利润百分比' )
    ladder = models.ForeignKey ( Ladder, on_delete=models.CASCADE, verbose_name='外键字段(阶梯)' )

    class Meta:
        db_table = 'tb_rank_sell'


# 运费模板表
class FreightManage ( BaseModel ):
    include_section = models.CharField ( default='', blank=True, max_length=40, verbose_name='包邮区域' )
    tname = models.CharField ( max_length=30, default='', verbose_name='模板名称' )
    include_section_no = models.CharField ( max_length=40, verbose_name='不包邮区域' )
    default_section = models.BooleanField ( default=False, verbose_name='是否设为默认模板' )
    freight_status = models.CharField ( default='', max_length=10, verbose_name='那方包邮(卖家,买家)' )
    more_money = models.DecimalField ( default=0, max_digits=6, decimal_places=2, verbose_name='续件价格' )
    initial_money = models.DecimalField ( default=0, max_digits=6, decimal_places=2, verbose_name='首件价格' )

    class Meta:
        db_table = 'tb_freight_manage'


# 城市邮费表
class CityPostage ( BaseModel ):
    freight = models.ForeignKey ( FreightManage, on_delete=models.CASCADE, verbose_name='模板外键' )
    area = models.CharField ( max_length=200, verbose_name='配送区域' )
    initial_money = models.DecimalField ( default=0, max_digits=6, decimal_places=2, verbose_name='首件价格' )
    more_money = models.DecimalField ( default=0, max_digits=6, decimal_places=2, verbose_name='续件价格' )

    class Meta:
        db_table = 'tb_city_postage'


# 采购表
class Procurement ( models.Model ):
    goods_name = models.CharField ( max_length=34, verbose_name='商品名称' )
    goods_color = models.CharField ( max_length=10, verbose_name='商品颜色' )
    cost = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='成本' )
    warehouse = models.CharField ( max_length=4, default='主仓库', verbose_name='仓库' )
    enter_time = models.DateTimeField ( auto_now_add=True, verbose_name='入库时间' )
    goodsNumber = models.ForeignKey ( GoodsStyle, on_delete=models.CASCADE, to_field='goodsNumber',
                                      verbose_name='外键字段(货号)' )
    sole = models.CharField ( default='', max_length=50, verbose_name='唯一串和商品数量表相同' )

    class Meta:
        db_table = 'tb_procurement'


class StockProcurement ( models.Model ):
    procurement = models.ForeignKey ( GoodsStyle, on_delete=models.CASCADE, to_field='goodsNumber', verbose_name='外键' )
    size = models.CharField ( default='', max_length=8, verbose_name='尺码' )
    stock = models.IntegerField ( default=0, verbose_name='单次库存' )
    sole = models.CharField ( default='', max_length=50, verbose_name='唯一串和商品数量表相同' )

    class Meta:
        db_table = 'tb_procurement_stock'


class Collect ( BaseModel ):
    spu = models.ForeignKey ( SPU, on_delete=models.CASCADE, verbose_name='商品外键id' )
    user = models.ForeignKey ( User, on_delete=models.CASCADE, verbose_name='用户外键id' )

    class Meta:
        db_table = 'tb_collect'
        verbose_name = '收藏表'


class Banner ( BaseModel ):
    banner_image_url = models.CharField ( max_length=200, verbose_name='banner图片地址' )
    banner_name = models.CharField ( max_length=200, verbose_name='图片名称' )
    sort = models.IntegerField ( verbose_name='排序' )
    spu_code = models.CharField ( max_length=50, verbose_name='spu编码' )
    is_start = models.IntegerField ( default=0, verbose_name='是否启用' )
    skip_type = models.CharField ( max_length=20, verbose_name='跳转类型' )

    class Meta:
        db_table = 'tb_banner'
        verbose_name = 'banner轮播图'


class GoodsNews ( BaseModel ):
    GOODS_NEWS_NOW_LIST = (
        (1, '首页最新'),
        (2, '首页一排一'),
        (3, '全部产品最新上市'),
        (4, '全部产品一排二'),
    )
    spu_code = models.ForeignKey ( SPU, to_field='spu_code', on_delete=models.CASCADE, verbose_name='spu编码' )
    goods_name = models.CharField ( max_length=100, verbose_name='商品名称' )
    sort = models.IntegerField ( verbose_name='排序字段' )
    type = models.SmallIntegerField ( choices=GOODS_NEWS_NOW_LIST, verbose_name='所属那个布局' )

    class Meta:
        db_table = 'tb_goods_news'
        verbose_name = '前端布局表'


# 布局模板'   例如: 鞋子-->凉鞋
class LayouTemplate ( BaseModel ):
    name = models.CharField ( max_length=30, verbose_name='前端布局模板名称' )
    image_url = models.CharField ( max_length=190, verbose_name='模板图片' )
    sort = models.IntegerField ( verbose_name='排序字段' )
    is_start = models.IntegerField ( default=0, verbose_name='是否启用' )

    class Meta:
        db_table = 'tb_template'


# 不同模板下的商品
class GoodsLayouTemplate ( BaseModel ):
    spu_code = models.ForeignKey ( SPU, to_field='spu_code', on_delete=models.CASCADE, verbose_name='spu编码' )
    temp = models.ForeignKey ( LayouTemplate, on_delete=models.CASCADE, verbose_name='外键模板id' )
    goods_name = models.CharField ( max_length=100, verbose_name='商品名称' )
    sort = models.IntegerField ( verbose_name='排序字段' )
    is_start = models.IntegerField ( default=0, verbose_name='是否启用' )

    class Meta:
        db_table = 'tb_template_goods'


# 布局模板' 热门--最新--...
class FromBlock ( BaseModel ):
    name = models.CharField ( max_length=30, verbose_name='前端布局模板名称' )
    sort = models.IntegerField ( verbose_name='排序字段' )
    is_start = models.IntegerField ( verbose_name='是否启用' )

    class Meta:
        db_table = 'tb_from_block'


# 不同模板下的商品
class FromGoods ( BaseModel ):
    spu_code = models.ForeignKey ( SPU, to_field='spu_code', on_delete=models.CASCADE, verbose_name='spu编码' )
    block = models.ForeignKey ( FromBlock, on_delete=models.CASCADE, verbose_name='外键模板id' )
    goods_name = models.CharField ( max_length=100, verbose_name='商品名称' )
    sort = models.IntegerField ( verbose_name='排序字段' )
    is_start = models.IntegerField ( default=0, verbose_name='是否启用' )

    class Meta:
        db_table = 'tb_from_goods'


# 热搜表
class TopSearch ( models.Model ):
    search_name = models.CharField ( max_length=40, verbose_name='搜索词' )
    search_count = models.IntegerField ( default=0, verbose_name='搜索次数' )
    serach_time = models.DateTimeField ( auto_now_add=True, verbose_name='搜索日期' )

    class Meta:
        db_table = 'tb_topsearch'


# 商家列表
class MerchantManage ( BaseModel ):
    ZGVIP_code = models.ForeignKey ( User, on_delete=models.CASCADE, to_field='ZGVIP_code', verbose_name='外键足购id' )
    name = models.CharField ( max_length=40, verbose_name='商家名称' )
    memo = models.CharField ( max_length=200, verbose_name='备忘录' )
    amount_money = models.DecimalField ( max_digits=10, default=0.00, decimal_places=2, verbose_name='商家所剩余额' )

    class Meta:
        db_table = 'tb_merchant_manage'


# 商家提现详情表
class DepositOut ( models.Model ):
    ZGVIP_code = models.CharField ( max_length=50, verbose_name='足购id' )
    name = models.CharField ( max_length=40, verbose_name='商家名称' )
    enter_time = models.DateTimeField ( auto_now_add=True )
    out_money = models.DecimalField ( max_digits=7, decimal_places=2, verbose_name='入库金额' )

    class Meta:
        db_table = 'tb_deposit_out'


# 退货地址表
class SalesReturn ( BaseModel ):
    name = models.CharField ( max_length=20, verbose_name='姓名' )
    phone = models.CharField ( max_length=20, verbose_name='联系方式' )
    address = models.CharField ( max_length=50, verbose_name='退货地址' )
    detail = models.CharField ( max_length=50, verbose_name='详细街道' )
    is_default = models.BooleanField ( default=False, verbose_name='是否默认' )

    class Meta:
        db_table = 'tb_sales_return'


# 店铺数据表
class RunData ( models.Model ):
    order_count = models.IntegerField ( default=0, verbose_name='当天订单总量' )
    run_amount = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='当天营业额' )
    refund_count = models.IntegerField ( default=0, verbose_name='当天退款单量' )
    refund_amount = models.DecimalField ( max_digits=10, decimal_places=2, verbose_name='当天退款总额' )
    date_time = models.DateTimeField ( auto_now_add=True, verbose_name='生成时间' )

    class Meta:
        db_table = 'tb_run_data'


# #管理员表
# class  Administrator(BaseModel):
#     username = models.CharField(max_length=20, verbose_name='管理员账号')
#     password = models.CharField(max_length=18, verbose_name='密码')
#     status = models.IntegerField(default=1, verbose_name='逻辑删除 0:不启用, 1:启用')
#
#
#     class Meta:
#         db_table = 'tb_admin_user'

# 管理员表
class Administrator ( BaseModel ):
    name = models.CharField ( max_length=15, verbose_name='员工名称' )
    username = models.CharField ( max_length=150, verbose_name='用户名称' )
    password = models.CharField ( max_length=200, verbose_name='用户密码' )
    status = models.BooleanField ( default=True, verbose_name='是否启用' )
    role = models.ForeignKey ( "Role", on_delete=models.SET_NULL, verbose_name='外键关联角色表', blank=True, null=True )

    class Meta:
        db_table = 'tb_admin_user'
        verbose_name = '管理员表'
        verbose_name_plural = verbose_name


# 角色表 ok
class Role ( BaseModel ):
    name = models.CharField ( unique=True, max_length=100, verbose_name='角色名称' )
    status = models.BooleanField ( default=True, verbose_name='是否启用' )

    class Meta:
        db_table = 'tb_role'
        verbose_name = '角色表'
        verbose_name_plural = verbose_name


#
class RoleAdministrator ( BaseModel ):
    role = models.ForeignKey ( 'Role', on_delete=models.CASCADE, verbose_name='角色外键' )
    admin = models.ForeignKey ( 'Administrator', on_delete=models.CASCADE, verbose_name='管理员外键' )

    class Meta:
        db_table = 'tb_role_admin'
        verbose_name = '资源权限表'


# 资源表
class Resource ( BaseModel ):
    name = models.CharField ( max_length=100, verbose_name='资源名称' )
    link_url = models.CharField ( max_length=200, default='', blank=True, null=True, verbose_name='跳转的url' )
    status = models.BooleanField ( default=True, verbose_name='是否启用' )
    pid = models.IntegerField ( verbose_name='二级嵌套id' )

    class Meta:
        db_table = 'tb_resource'
        verbose_name = '资源表'
        verbose_name_plural = verbose_name


# 资源权限
class ResourcePermissions ( BaseModel ):
    admin = models.CharField ( max_length=20, verbose_name="资源权限" )

    class Meta:
        db_table = 'tb_resource_permissions'
        verbose_name = '权限表'


# 多对多, 资源--权限
class ResourceAdmin ( BaseModel ):
    pid = models.ForeignKey ( 'Resource', on_delete=models.CASCADE, verbose_name='角色外键' )
    admin = models.ForeignKey ( 'ResourcePermissions', on_delete=models.CASCADE, verbose_name='资源外键' )

    class Meta:
        db_table = 'tb_resource_admin'
        verbose_name = '资源权限表'


# 角色资源权限表
class RoleResource ( BaseModel ):
    role = models.ForeignKey ( 'Role', on_delete=models.CASCADE, verbose_name='角色外键' )
    resource = models.ForeignKey ( 'Resource', on_delete=models.CASCADE, verbose_name='菜单资源外键' )
    pid = models.CharField ( max_length=150, verbose_name='当前菜单拥有哪些资源', blank=True )
    admin = models.CharField ( max_length=50, verbose_name='当前资源拥有哪些权限', blank=True )

    class Meta:
        db_table = 'tb_role_resource'
        verbose_name = '角色资源表'
        verbose_name_plural = verbose_name


# 资源选择状态表
class SelectResource ( models.Model ):
    status = models.TextField ( max_length=500, verbose_name='选择状态' )
    role_id = models.IntegerField ( verbose_name='角色外键' )

    class Meta:
        db_table = 'tb_select_resource'
