from django.contrib import admin
from .models import Category,Product,Order,Custmer

# Register your models here.
@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ['id','name','price','category']


@admin.register(Order)
class orderadmin(admin.ModelAdmin):
    list_display=['product','custmer','quantity','price','adress', 'phone']


@admin.register(Custmer)
class custmeradmin(admin.ModelAdmin):
    list_display=['id','email','password']
