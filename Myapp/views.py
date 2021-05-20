
from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Product,Category,Order,Custmer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import sessions
from django.contrib.auth.hashers import  check_password

# Create your views here.
def index(request):
    if request.method =="POST":
        product = request.POST.get('product')
        remove=request.POST.get('remove')
        
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                  cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1 
            else:
                cart[product] = 1
        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
     
        if cart == 0:
            messages.info(request,'Cart is empty')
        return HttpResponseRedirect("/")
    else:
        cart=request.session.get('cart')
        if not cart:
            request.session.cart ={}
    products=None
    categories=Category.allcategory()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.allproductid(categoryID)
    else:
        products=Product.allproduct()

    return render(request,'Myapp/index.html',{"products":products,"categories":categories})
def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        form=Custmer(email=email,password=password)
        form.save()
        messages.success(request,"Sucessfull")

       
       
    else:
        form=Custmer()
    return render(request,'Myapp/signup.html')
def user_log(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        custmer = Custmer.get_custmer_by_email(email)
        error_message = None
        if custmer:
            flag = check_password(password, custmer.password)
            if flag:
                request.session['custmer'] = custmer.id

            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'Myapp/login.html')

   
    else:

     
      return render(request , 'Myapp/login.html')
    
     
        
            
  


def log(request):
    logout(request)
    return HttpResponseRedirect('/')

def cartitem(request):
   

    ids= list(request.session.get('cart').keys())
    products=Product.cartid(ids)
    
    return render(request,'Myapp/cart.html',{"products":products})

def deletedata(request,id):
    if request.method=="POST":
          form=Product.objects.get(pk=id)
          form.delete()
          return HttpResponseRedirect("/cart/")
  
def checkout(request):
    if request.method=="POST":
        adress=request.POST.get('adress')
        phone=request.POST.get('phone')
        #- user=request.user.get_username.id
        cart=request.session.get('cart')
        products=Product.cartid(list(cart.keys()))
        print(adress,phone,cart,products)
        for product in products:
               order=Order(product=product,custmer=User(id=request.user.get_username),price=product.price,quantity=cart.get(str(product.id)),adress=adress,phone=phone)
               order.save()
    
    return redirect('/cart/')  
   
   

   