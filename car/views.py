from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Person, Car
from .serializers import PersonSer, CarSer, CarReadSer
from rest_framework import viewsets, permissions


# @api_view(["GET", "POST"])
# def Pesrson_View(request):
#     if request.method == "GET":
#         person = Person.objects.all()
#         return Response(PersonSer(person, many=True).data
#                         , status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         ser = PersonSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class personViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSer
    http_method_names = ['get', 'post', 'delete', 'put']

    search_fields = ('name',)
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        obj = super().list(request, *args, **kwargs)
        print("----list____")
        return obj

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("----creat____")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("______update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("______retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("______destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj


# @api_view(["GET", "POST"])
# def Car_View(request):
#     if request.method == "GET":
#         car = Car.objects.all()
#         return Response(CarSer(car, many=True).data
#                         , status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         ser = CarSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CarSer
        else:
            return CarReadSer
from django.shortcuts import render

# Create your views here.
