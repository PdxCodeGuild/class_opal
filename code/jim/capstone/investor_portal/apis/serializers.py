from rest_framework import serializers
from personalized_index import models
from io import BytesIO
import matplotlib.pyplot as plt


class PersonalizedIndexSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        fields = (
            'user',
            'id',
            'index_name',
            'index_allocation',
            'market_cap_min',
            'dividend_yield_min',
            'pe_ratio_max',
            'sector_exclude_1',
            'sector_exclude_2',
        )
        model = models.PersonalizedIndex


class PersonalizedIndexStockSerializer(serializers.ModelSerializer):
    symbol_id = serializers.ReadOnlyField()
    personalized_index_id = serializers.ReadOnlyField()

    class Meta:
        fields = (
            'symbol_id',
            'position_weight',
            'target_allocation',
            'current_price',
            'quantity',
            'order_quantity',
            'rounding_loss',
            'personalized_index_id',
        )
        model = models.PersonalizedIndexStock


class CashFlowPlanSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def to_representation(self, instance):
        image = BytesIO()
        plt.savefig(image, format='png')
        return {'image': image.getvalue()}
