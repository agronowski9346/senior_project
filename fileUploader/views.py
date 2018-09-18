from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from fileUploader.models import Product
# Create your views here.
 
 
 
@api_view(['GET'])
def view_books(request):
    p = Product(name='test',description='test',price=3, date_created='2016-06-22 19:10:25-07', date_modified ='2016-06-22 19:10:25-07')
    p.save()
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status=status.HTTP_201_CREATED)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")