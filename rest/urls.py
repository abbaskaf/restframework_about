from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restapp.urls')),
    path('employ/', include('employ.urls')),
    path('car/', include('car.urls'))

]
