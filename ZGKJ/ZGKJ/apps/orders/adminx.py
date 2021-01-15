# import xadmin
# from xadmin import views
#
# from . import models
#
#
# class LogisticsInfoAdmin(object):
#     # 给该模型类增加图标
#     model_icon = 'fa fa-gift'
#     # 指定该模型类显示的字段
#     list_display = ('id', 'out_trade_no', 'logistics_no')
#     # 搜索和搜索框显示
#     search_fields = ['logistics_no', 'out_trade_no']  # 控制搜索框的显示
#     # list_filter = ['pkey', 'pkey_desc', 'pvalue', 'pvalue_desc']  # 控制筛选
#
#
# xadmin.site.register(models.LogisticsInfo, LogisticsInfoAdmin)
#
# """
# admin的语法
#     admin.site.register(models.SKUImage)
#
# xadmin的语法
#     xadmin.site.register(models.SKUImage)
# """
