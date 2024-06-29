from rest_framework import serializers
from .models import Category,Product,Color


class ColorSerializer(serializers.ModelSerializer):
     class Meta:
          model = Color
          fields = ('color', )


class ProductSerializer(serializers.ModelSerializer):
     colors = ColorSerializer(many=True, read_only=True)
     class Meta:
        model = Product
        fields = ('product','name', 'img', 'price', 'colors' )


class CategorySerializer(serializers.ModelSerializer):

     products = ProductSerializer(many=True, read_only=True)

     class Meta:
        model = Category
        fields = ('name', 'products', )