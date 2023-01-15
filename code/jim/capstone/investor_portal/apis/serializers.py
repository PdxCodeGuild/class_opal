from rest_framework import serializers
from personalized_index import models


class PersonalizedIndexSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user',
            'index_name',
            'index_allocation',
            'market_cap_min',
            'dividend_yield_min',
            'pe_ratio_max',
            'sector_exclude_1',
            'sector_exclude_2',
        )
        model = models.PersonalizedIndex
