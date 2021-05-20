
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def allcategory():
        return Category.objects.all()



class Product(models.Model):
    name = models.CharField( max_length=50)
    price =models.IntegerField()
    category =models.ForeignKey(Category,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    des = models.TextField()

    def __str__(self):
        return self.name
    

    
    @staticmethod
    def cartid(ids):
        return Product.objects.filter(id__in=ids)




    @staticmethod
    def allproduct():
        return Product.objects.all()

    
    @staticmethod
    def allproductid(category):
        if category:
            return Product.objects.filter(category=category)
        else:
            return Product.allproduct()
        


 

    

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    custmer=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    adress=models.CharField( max_length=50)
    phone= models.CharField(max_length=50)
    date=models.DateField(default=datetime.today)
   
class Custmer(models.Model):
    email=models.EmailField( max_length=254)
    password=models.CharField(max_length=100 )

    
    @staticmethod
    def get_custmer_by_email(email):
        try:
            return Custmer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Custmer.objects.filter(email = self.email):
            return True

        return  False

