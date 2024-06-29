from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField('Category name')

    def __str__(self):
        return self.name
    

class Color(models.Model):
    color = models.CharField('Color', max_length=20)

    def __str__(self):
        return self.color


    
class Product(models.Model):
    product = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Product name', max_length=60)
    img = models.ImageField('Product image', upload_to='product_img')
    price = models.PositiveIntegerField('Product price')
    colors = models.ManyToManyField(Color)

    def __str__(self):
        return self.name