# from django.db import models
# from ZGKJ.utils.models import BaseModel
# from goods.models import SKU
#
#
# # Create your models here.
# class User(BaseModel):
#     """自定义用户模型类"""
#     nickName = models.CharField(max_length=200, verbose_name='微信昵称')
#     gender = models.IntegerField(default=1, verbose_name='性别')  # 1男2女
#     language = models.CharField(max_length=10, verbose_name='语言')
#     wx_city = models.CharField(max_length=50, verbose_name='城市')
#     wx_province = models.CharField(max_length=50, verbose_name='省')
#     wx_country = models.CharField(max_length=50, verbose_name='国家')
#     avatarUrl = models.CharField(max_length=200, verbose_name='头像url')
#     star = models.ManyToManyField(SKU, blank=True, verbose_name='收藏', default='')
#     openId = models.CharField(unique=True, max_length=30, verbose_name='小程序用户openid')
#     # 默认地址
#     default_area = models.IntegerField(default=0, blank=True, verbose_name='默认收货地址')
#
#     # 邀请码
#     invitationCode = models.CharField(default='', max_length=16, verbose_name='邀请码')
#     invite_user_id = models.IntegerField(default=0, verbose_name="邀请人ID")
#     invite_nickname = models.CharField(default='', max_length=100, verbose_name="邀请人昵称")
#     onroad = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, verbose_name="在途货款")
#     balance = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, verbose_name="余额")
#
#     # password = models.CharField(max_length=16, verbose_name='密码')
#     class Meta:
#         db_table = 'tb_users'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name
#
#
# class Invitation(BaseModel):
#     user_id = models.CharField(max_length=8, verbose_name='用户ID')
#     invitationCode = models.CharField(max_length=16, verbose_name='用户邀请码')
#     invitatePersonID = models.CharField(max_length=10, verbose_name='邀请人')
#     invitatePersonCode = models.CharField(max_length=16, verbose_name='邀请人码')
#     balance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='余额')
#     expense = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='花费')
#
#     class Meta:
#         db_table = 'tb_invitation'
#         verbose_name = '邀请表'
#         verbose_name_plural = verbose_name
