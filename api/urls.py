from django.urls import include, path
from django.conf.urls import url

from .views import RoomListView, RoomDetailView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', RoomListView.as_view()),
    path('<pk>', RoomDetailView.as_view()),
]
