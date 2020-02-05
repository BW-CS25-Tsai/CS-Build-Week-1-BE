from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
# from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    # path('login/', views.obtain_auth_token, name='auth')
]
