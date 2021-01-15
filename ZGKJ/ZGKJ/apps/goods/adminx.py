# import xadmin
# from xadmin import views
#
# from . import models
#
# from xadmin.plugins.actions import BaseActionView
#
#
# class StatusReverseAction(BaseActionView):
#     action_name = u"reverse_active"
#     description = u'将激活状态变为相反'
#     model_perm = 'change'
#
#     def do_action(self, queryset):
#         for obj in queryset:
#             obj.active = not obj.active
#             obj.save()
#
#
# class BaseSetting(object):
#     """xadmin的基本配置"""
#     enable_themes = True  # 开启主题切换功能
#     use_bootswatch = True
#
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
#
#
# class GlobalSettings(object):
#     """xadmin的全局配置"""
#
#     def get_site_menu(self):  # 名称不能改
#         return [
#             {
#                 'title': '自定义后台',
#                 'icon': 'fa fa-bar-chart-o',
#                 'menus': (
#                     {
#                         'title': '退货单',  # 这里是你菜单的名称
#                         'url': '/xadmin/test_view',  # 这里填写你将要跳转url
#                         'icon': 'fa fa-cny'  # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
#                     },
#                     {
#                         'title': '提现单',
#                         'url': 'http://www.taobao.com',
#                         'icon': 'fa fa-cny'
#                     },
#                     {
#                         'title': '添加商品',
#                         'url': 'http://www.taobao.com',
#                         'icon': 'fa fa-cny'
#                     }
#                 )
#
#             }
#         ]
#
#     site_title = "足购商城管理员后台"  # 设置站点标题
#     site_footer = "足购科技有限公司"  # 设置站点的页脚
#     menu_style = "accordion"  # 设置菜单折叠
#
#
# xadmin.site.register(views.CommAdminView, GlobalSettings)
#
#
# class SizeInline(object):
#     model = models.GoodsSize
#     extra = 0
#
#
# class SKUAdmin(object):
#     # actions = [StatusReverseAction]
#     # 还原按钮
#     # reversion_enable = True
#
#     # 给该模型类增加图标
#     model_icon = 'fa fa-gift'
#     # 指定该模型类显示的字段
#     list_display = ('id', 'name', 'price', 'sales', 'goodsNumber', 'go_to')
#     # 搜索和搜索框显示
#     search_fields = ['name', 'goodsNumber']  # 控制搜索框的显示
#
#     # inlines = [SizeInline]
#     # list_filter = ['pkey', 'pkey_desc', 'pvalue', 'pvalue_desc']  # 控制筛选
#     # 过滤不同用户的录入信息，只能修改自己的信息
#     def save_models(self):
#         self.new_obj.user = self.request.user
#         super().save_models()
#
#     def queryset(self):
#         qs = super(SKUAdmin, self).queryset()
#         if self.request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(_user=self.request.user)
#
#
# xadmin.site.register(models.GoodsCategory)
# xadmin.site.register(models.GoodsSize)
# xadmin.site.register(models.Goods)
# xadmin.site.register(models.Brand)
# xadmin.site.register(models.SKU, SKUAdmin)
#
# """
# admin的语法
#     admin.site.register(models.SKUImage)
#
# xadmin的语法
#     xadmin.site.register(models.SKUImage)
# """
