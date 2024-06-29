from django.shortcuts import render
from .models import Category,Product, Color
from rest_framework import viewsets
from .serializers import CategorySerializer,ProductSerializer,ColorSerializer
# Create your views here.
 

class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViews(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViews(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer