from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employ
from .serializers import EmploySer


@api_view(["POST"])
def Post_Employ(request):
    data = {
        "name": request.data["name"],
        "age": request.data["age"],
        "salary": request.data["salary"],
        "post": request.data["post"],
    }
    ser = EmploySer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def List(request):
    dj = Employ.objects.all()
    ser = EmploySer(dj, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def Gpd(request, pk):
    try:
        employee = Employ.objects.get(pk=pk)
    except:
        return request({"errors": "Not_Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = EmploySer(employee)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        ser = EmploySer(employee, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
