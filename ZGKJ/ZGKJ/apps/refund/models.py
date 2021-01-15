# from django.db import models
#
# # Create your models here.
# # 退款订单
# from ZGKJ.utils.models import BaseModel
#
#
# class RefundOrder(BaseModel):
#     """退货订单表"""
#     ORDER_STATUS_CHOICES = (
#         (1, "审核中"),
#         (2, "待买家发货"),
#         (3, "待卖家收货"),
#         (4, "待退款"),
#         (5, "已完成"),
#         (6, "已取消"),
#         (7, "审核不通过"),
#     )
#     user_id = models.IntegerField(verbose_name="用户id")
#     out_refund_no = models.CharField(max_length=64, verbose_name="退货订单号")
#     out_trade_no = models.CharField(max_length=64, verbose_name="订单号")
#     order_amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="订单金额")
#     refund_amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="退款金额")
#     is_refund = models.BooleanField(default=False, verbose_name="是否已退款")
#     status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name="退款订单状态")
#     not_pass_reason = models.CharField(max_length=200, verbose_name="审核不通过原因", blank=True, null=True)
#     refund_reason = models.CharField(max_length=255, verbose_name="退款原因", blank=True, null=True)
#     is_delete = models.BooleanField(default=False)
#     re_type = models.SmallIntegerField(verbose_name="退货类型")
#     logistics_no = models.CharField(max_length=64, verbose_name="运单号", blank=True, null=True)
#     logistics_company = models.SmallIntegerField(verbose_name="物流公司id", blank=True, null=True)
#
#     class Meta:
#         db_table = 't_refund'
#         verbose_name = '退款表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return "{}退款{}".format(self.out_trade_no, self.refund_amount)
#
#     # 验证是否已经退款
#     def save(self, *args, **kwargs):
#         if self.is_refund:
#             return "{}已经退过款了！".format(self.out_trade_no)
#
#         super(RefundOrder, self).save(*args, **kwargs)  # Call the "real" save() method.
#
# #-------------------此表还未创建------------------------
# # 退款物流信息
# class LogisticsInfo(BaseModel):
#     """退款物流信息"""
#     LOGISTICS_COMPANY = {"顺丰": "SFEXPRESS",
#                          "申通": "STO",
#                          "韵达": "YUNDA",
#                          "中通": "ZTO"}
#
#     out_refund_no = models.CharField(max_length=50, verbose_name='退款订单号')
#     logistics_no = models.CharField(max_length=50, verbose_name='运单号')
#     logistics_company = models.CharField(max_length=20, verbose_name='物流公司代码', blank=True, null=True)
#
#     class Meta:
#         db_table = 'tb_refund_logistic_info'
#         verbose_name = "退款订单物流信息"
#         verbose_name_plural = verbose_name
