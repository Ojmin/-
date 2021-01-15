# from django.db import models
#
# # Create your models here.
# from ZGKJ.utils.models import BaseModel
#
#
# # 邀请明细表
# class Invitation(BaseModel):
#     user_id = models.IntegerField(verbose_name='用户ID')
#     user_nickname = models.CharField(max_length=32, verbose_name='邀请人昵称')
#     invite_user_id = models.IntegerField(verbose_name='邀请人')
#     invite_nickname = models.CharField(max_length=32, verbose_name='邀请人昵称')
#     invite_user_code = models.CharField(max_length=64, verbose_name="邀请人邀请码")
#     order_num = models.CharField(max_length=64, verbose_name="订单号")
#     product_name = models.CharField(max_length=100, verbose_name='商品名称')
#     volume = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='订单金额')
#     commission = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="提成")
#     code = models.CharField(max_length=64, verbose_name="用户邀请码")
#     status = models.BooleanField(default=False)  # 在途货款是否转到balance
#
#     class Meta:
#         db_table = 't_invitation'
#         verbose_name = '邀请明细记录表'
#         verbose_name_plural = verbose_name
#         ordering = ['id']
#
#
# # 提现记录明细表
# class TWithdrawCash(BaseModel):
#     order_num = models.CharField(max_length=64, verbose_name="订单号")
#     user_id = models.IntegerField(verbose_name="用户id")
#     amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="提现金额")
#     status = models.SmallIntegerField(default=0, verbose_name="提现是否已支付")
#
#     class Meta:
#         db_table = 't_withdraw_cash'
#         verbose_name = '提现明细记录表'
#         verbose_name_plural = verbose_name
#         ordering = ['id']
