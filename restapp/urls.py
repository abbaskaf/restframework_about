from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('hi', views.hello),
    # path('Calculater', views.Calculater),
    path('cal', views.cal)
]
