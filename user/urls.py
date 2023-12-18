from django.urls import path
from .import views

urlpatterns = [
    path('post_user',views.creat_user),
]