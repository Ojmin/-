# from django.db import models
#
# # Create your models here.
# # 退款信息
# from ZGKJ.utils.models import BaseModel
#
#
# class RefundInfo(BaseModel):
#     """退货"""
#     STATUS = (
#         (1, "待审核"),
#         (2, "审核通过"),
#         (3, "等待买家发货"),
#         (4, "等待商家确认收货"),
#         (5, "已完成"),
#     )
#     out_trade_no = models.CharField(max_length=50, verbose_name='退款单号')
#     out_refund_no = models.CharField(max_length=50, verbose_name='退款单号')
#     total_fee = models.CharField(max_length=20, verbose_name='订单金额')
#     refund_fee = models.CharField(max_length=20, verbose_name='退款金额')
#     cause = models.CharField(max_length=500, verbose_name='退货理由')
#     status = models.SmallIntegerField(choices=STATUS, default=1, verbose_name="订单状态")
#
#     class Meta:
#         db_table = 'tb_refund_info'
#         verbose_name = "退款信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '%s:退款 %s 成功' % (self.out_refund_no, self.refund_fee)
