from goods.models import RefundOrder
from rest_framework import serializers


class RefundModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefundOrder
        fields = "__all__"


class RefundSerializers(serializers.Serializer):
    user_id = serializers.IntegerField (  )
    out_refund_no = serializers.CharField ( )
    order_sn = serializers.CharField (  )
    order_amount = serializers.DecimalField ( decimal_places=2, max_digits=10)
    refund_amount = serializers.DecimalField ( decimal_places=2, max_digits=10)
    is_refund = serializers.BooleanField ( default=False)
    status = serializers.IntegerField (default=1 )
    not_pass_reason = serializers.CharField (default='')
    refund_reason = serializers.CharField ( )
    is_delete = serializers.BooleanField ( default=False )
    re_type = serializers.IntegerField ( )
    logistics_no = serializers.CharField (default='')
    logistics_company = serializers.IntegerField (default=0)

    def create(self, data):
        refund = RefundOrder.objects.create(**data)
        return refund

