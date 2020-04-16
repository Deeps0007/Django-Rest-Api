from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@api_view(['GET'])
def hello(request):
    return render(request, "products/hello.html", {})


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        obj = Product.objects.all()
        serailizer = ProductSerializer(obj, many=True)
        return Response(serailizer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def single_product_detail(request, pk):
    try:
        obj = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Message(APIView):

    def get(self, request):
        return Response(data="Hello this is Class based view hit by GET Request", status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data="This is class based view hit by POST request", status=status.HTTP_200_OK)
