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
from django.shortcuts import get_object_or_404
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

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#process POST request to register a user
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        try:
            user = User('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x')
            print(request.POST.get("username"))
            user = User(username=request.POST.get("username"), email = request.POST.get("email"), first_name = request.POST.get("first_name"), last_name = request.POST.get("last_name"), password=make_password(request.POST.get("password")), phone_number = request.POST.get("phone_number"), home_address = request.POST.get("home_address"))
            user.save()
        except Exception as e:
            return Response('', status=status.HTTP_201_CREATED)
        return Response('', status=status.HTTP_400_BAD_REQUEST)
    return Response('', status=status.HTTP_200_OK)