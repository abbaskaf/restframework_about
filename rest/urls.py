from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restapp.urls')),
    path('employ/', include('employ.urls')),
    path('car/', include('car.urls')),

    path('api-token-auth', views.obtain_auth_token),
    path('api-auth', include('rest_framework.urls')),
]
