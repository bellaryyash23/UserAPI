from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# GET all User's Details
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)
    return Response({"Users": user_serializer.data}, status=status.HTTP_200_OK)


# ADD a new user
@api_view(['POST'])
def add_user(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response({"New User Id": user_serializer.data['id']}, status=status.HTTP_201_CREATED)
    else:
        return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


# LOGIN existing user
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    try:
        User.objects.get(username=username) and User.objects.get(password=password)
        valid = True
    except User.DoesNotExist:
        valid = False

    if valid:
        return Response({"Success": "Login Successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"Error": "User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
