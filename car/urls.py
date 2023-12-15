from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person', views.personViewset)
router.register('car',views.CarView)
urlpatterns = [
    # path('get_car', views.Car_View),
    # path('get_person', views.Pesrson_View),

]

urlpatterns += router.urls
