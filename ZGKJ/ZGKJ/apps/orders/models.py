# # Create your models here.
#
#
# from django.db import models
#
# from ZGKJ.utils.models import BaseModel
# from areas.models import UserAcceptGoodAreaModel
#
#
# # Create your models here.
#
#
# class OrderInfo(BaseModel):
#     """
#     订单信息
#     """
#
#     ORDER_STATUS_ENUM = {
#         "UNPAID": 1,
#         "UNSEND": 2,
#         "UNRECEIVED": 3,
#         "FINISHED": 4,
#     }
#
#     ORDER_STATUS_CHOICES = (
#         (1, "待支付"),
#         (2, "待发货"),
#         (3, "待收货"),
#         (4, "已完成"),
#         (5, "已取消"),
#         (6, "退款中"),
#         (7, "已退款")
#     )
#
#     # 1.23   float 1.2299999999
#     # 1.23   Decimal   1   23     1.23
#     out_trade_no = models.CharField(unique=True, max_length=64, primary_key=True, verbose_name="订单号")
#     goodsNumber = models.CharField(max_length=64, verbose_name='订单号')
#     title = models.CharField(max_length=20, verbose_name='标题')
#     # subTitle = models.CharField(max_length=150,verbose_name='副标题')
#     image = models.CharField(max_length=200, verbose_name='图片路径')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
#     size = models.CharField(max_length=5, verbose_name='尺码')
#     user_id = models.IntegerField(verbose_name="下单用户ID")
#     address = models.ForeignKey(UserAcceptGoodAreaModel, on_delete=models.PROTECT, verbose_name="收获地址")
#     total_count = models.IntegerField(default=1, verbose_name="商品总数")
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额")
#     freight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="运费")
#     status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name="订单状态")
#     is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')
#     # 为提现加
#     user_nickname = models.CharField(max_length=32, verbose_name="用户昵称")
#     invite_user_id = models.IntegerField(verbose_name="邀请人id")
#     invite_nickname = models.CharField(max_length=32, verbose_name="邀请人昵称")
#
#     class Meta:
#         db_table = "tb_order_info"
#         verbose_name = '订单基本信息'
#         verbose_name_plural = verbose_name
#
#
# # 物流信息
# class LogisticsInfo(BaseModel):
#     out_trade_no = models.CharField(max_length=50, verbose_name='订单号')
#     logistics_no = models.CharField(max_length=50, verbose_name='运单号')
#     logistics_company = models.CharField(max_length=20, verbose_name='物流公司代码', blank=True, null=True)
#
#     class Meta:
#         db_table = 'tb_logistic_info'
#         verbose_name = "订单物流信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         order = OrderInfo.objects.get(out_trade_no=self.out_trade_no)
#         order.status = 3
#         order.save()
#         return '%s:录入运单号 %s 成功' % (self.out_trade_no, self.logistics_no)
