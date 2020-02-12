from rest_framework import serializers
from adventure.models import Room, Player
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('title', 'description', 'n_to',
        's_to', 'e_to', 'w_to','x','y')
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('user', 'currentRoom', 'uuid',)