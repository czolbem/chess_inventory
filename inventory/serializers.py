from rest_framework import serializers

from inventory.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['url', 'pgn', 'description', 'event', 'site', 'date', 'round', 'white', 'black', 'result', 'eco',
                  'opening', 'variation', 'ecot', 'openingt', 'variationt']
        read_only_fields = ['event', 'site', 'date', 'round', 'white', 'black', 'result', 'eco', 'opening', 'variation',
                            'ecot', 'openingt', 'variationt']
