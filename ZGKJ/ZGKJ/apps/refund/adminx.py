# import xadmin
# from . import models
#
#
# class RefundAdmin(object):
#     # 给该模型类增加图标
#     model_icon = 'fa fa-gift'
#     # 指定该模型类显示的字段
#     list_display = ('id', 'out_refund_no', 'out_trade_no', "order_amount", "refund_amount", "status")
#     # 搜索和搜索框显示
#     search_fields = ['out_refund_no', 'out_trade_no', "status"]  # 控制搜索框的显示
#     # list_filter = ['pkey', 'pkey_desc', 'pvalue', 'pvalue_desc']  # 控制筛选
#     readonly_fields = ('out_refund_no', "status","is_refund",'out_trade_no', 'order_amount')
#
#
# xadmin.site.register(models.RefundOrder, RefundAdmin)
