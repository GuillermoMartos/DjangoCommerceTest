from django.db import models

# Create your models here.
# clase con parámetro es herencia, vamos a pasarle los métodos de models.Model a Products
class MiProducto(models.Model):
    name=models.CharField(max_length=230)
    price=models.FloatField()
    stock=models.IntegerField()
    img=models.CharField(max_length=530)
    
    
class MiOferta(models.Model):
    code = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    discount = models.FloatField()
    
    