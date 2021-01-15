from haystack import indexes

from .models import SPU


class SPUIndex(indexes.SearchIndex, indexes.Indexable):
    """
    SKU索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)
    print(text)
    def get_model(self):
        """返回建立索引的模型类"""
        return  SPU

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()
        # return self.get_model().objects.filter(is_launched=True)
