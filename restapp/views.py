from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Ser
#hello

@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({"massage": "hello,world"})


@api_view(['GET', 'POSt'])
def hello(request):
    if request.method == "GET":
        return Response({"massage": "hi ,world"})
    elif request.method == "POST":
        return Response({"massage": "hello ,{}".format(request.data["name"])})


# @api_view(["POST"])
# def Calculater(request):
    # try:
    #     num1 = request.data["num1"]
    #     num2 = request.data["num2"]
    #     opr = request.data["opr"]
    # except:
    #     return Response({"erorr massage": "send num1 and num2 and opr"}, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     if isinstance(num1, int) and isinstance(num2, int):
    #         if opr == "add":
    #             return Response({"result": num1 + num2}, status=status.HTTP_200_OK)
    #         elif opr == "sub":
    #             return Response({"result": num1 - num2}, status=status.HTTP_200_OK)
    #         elif opr == "div":
    #             return Response({"result": num1 / num2}, status=status.HTTP_200_OK)
    #         elif opr == "mul":
    #             return Response({"result": num1 * num2}, status=status.HTTP_200_OK)
    #
    #
    #         else:
    #             return Response({"error_massage": "send valid "}, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response({"error_massage": "send integer values"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def cal(request):
    post = Ser(data=request.data)

    if post.is_valid():
        num1 = post.data['num1']
        num2 = post.data['num2']
        opr = post.data['opr']
        if opr == "add":
                    return Response({"result": num1 + num2}, status=status.HTTP_200_OK)
        elif opr == "sub":
                    return Response({"result": num1 - num2}, status=status.HTTP_200_OK)
        elif opr == "div":
                    return Response({"result": num1 / num2}, status=status.HTTP_200_OK)
        elif opr == "mul":
                    return Response({"result": num1 * num2}, status=status.HTTP_200_OK)
        else:
                    return Response({"error_massage": "send valid "}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(post.errors,status=status.HTTP_400_BAD_REQUEST)
