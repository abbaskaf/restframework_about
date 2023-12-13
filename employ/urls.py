from django.urls import path
from . import views

urlpatterns = [
    path('post', views.Post_Employ),
    path('list', views.List),
    path('get/<int:pk>',views.Gpd),
]
