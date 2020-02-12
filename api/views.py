from rest_framework.generics import ListAPIView, RetrieveAPIView
from adventure.models import Room, Player
from .serializers import RoomSerializer , PlayerSerializer
class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class PlayerListView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
class PlayerDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer 