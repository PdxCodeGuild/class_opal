from rest_framework import serializers
from pokemon.models import Pokemon, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)


class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight',
                  'image_front', 'image_back', 'caught_by', 'types')


# class PokemonSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'number',
#             'name',
#             'height',
#             'weight',
#             'image_front',
#             'image_back',
#             'caught_by',
#         )
#         model = models.Pokemon


# class TypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'type',
#             'pokemon',
#         )
#         model = models.Type
