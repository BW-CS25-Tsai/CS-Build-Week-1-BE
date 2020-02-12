from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from adventure.api import RoomViewSet, PlayerViewSet
from .views import RoomListView, RoomDetailView, PlayerListView, PlayerDetailView

router = routers.DefaultRouter()
router.register(r'room', RoomViewSet)
router.register(r'player', PlayerViewSet)

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', RoomListView.as_view()),
    path('<pk>', RoomDetailView.as_view()),
    path('', PlayerListView.as_view()),
    path('<pk>', PlayerDetailView.as_view()),
    # path('', RoomViewSet.as_view),
    # path('<pk>', RoomViewSet.as_view),
    # path('', PlayerViewSet.as_view),
    # path('<pk>', PlayerViewSet.as_view),
]
