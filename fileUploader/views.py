from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import routers, serializers, viewsets
from fileCloud.serializers import UserSerializer
from fileUploader.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
#from fileUploader.models import Product   ;sample
# Create your views here.
 
 
'''
 samples 
@api_view(['GET'])
def view_books(request):
    p = Product(name='test',description='test',price=3, date_created='2016-06-22 19:10:25-07', date_modified ='2016-06-22 19:10:25-07')
    p.save()
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#process POST request to register a user
@api_view(['PUT'])
def register_user(request):
    if request.method == 'PUT':
        try:
            user = User('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x')
            print(request.PUT.get("username"))
            user = User(username=request.PUT.get("username"), email = request.PUT.get("email"), first_name = request.PUT.get("first_name"), last_name = request.POST.get("last_name"), password=make_password(request.PUT.get("password")), phone_number = request.PUT.get("phone_number"), home_address = request.PUT.get("home_address"))
            user.save()
        except Exception as e:
            return Response('', status=status.HTTP_201_CREATED)
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    return Response('', status=status.HTTP_200_OK)