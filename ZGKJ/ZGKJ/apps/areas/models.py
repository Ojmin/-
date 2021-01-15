# from django.db import models
#
# # Create your models here.
# from ZGKJ.utils.models import BaseModel
#
#
# class Area(models.Model):
#     """
#     行政区划
#     """
#     name = models.CharField(max_length=20, verbose_name='名称')
#     parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True,
#                                verbose_name='上级行政区划')
#
#     # 如果不自定义关联字段 related_name='subs',
#     # 那么默认的关联字段就是 area_set
#
#     class Meta:
#         db_table = 'tb_areas'
#         verbose_name = '行政区划'
#         verbose_name_plural = '行政区划'
#
#     def __str__(self):
#         return self.name
#
#
# class UserAcceptGoodAreaModel(BaseModel):
#     user_id = models.IntegerField(verbose_name='用户id')
#     AcceptPerson = models.CharField(max_length=10, verbose_name='收货人')
#     province = models.CharField(max_length=10, verbose_name='省')
#     city = models.CharField(max_length=10, verbose_name='市')
#     district = models.CharField(max_length=10, verbose_name='区')
#     place = models.CharField(max_length=50, verbose_name='地址')
#     mobile = models.CharField(max_length=11, verbose_name='手机')
#     is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')
#
#     class Meta:
#         db_table = 'tb_user_good_areas'
#         verbose_name = '用户收货地址'
#         verbose_name_plural = '该用户的收货地址'
#
#     def __str__(self):
#         return self.user_id + '：添加地址成功'
