from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.orders import Order
#middleware
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

from .forms import SignupForm,loginform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.contrib.auth.models import User

#Paginator
from django.core.paginator import Paginator
# Create your views here.
class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products=None
        categorys=Category.objects.all()
        cID=request.GET.get('category')
        if(cID):
            products=Product.objects.filter(category=cID)
        else:
            products=Product.objects.all()
        paginator=Paginator(products,27)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'index.html',{'products':page_obj,'categorys':categorys})

    def post(self,request):
        pid=request.POST.get('prd')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if(cart):
            quantity=cart.get(pid)
            if(quantity):
                if(remove):
                    if(quantity<=1):
                        cart.pop(pid)
                    else:
                        cart[pid]=quantity-1
                else:
                    cart[pid]=quantity+1
            else:
                cart[pid]=1
        else:
            cart={}
            cart[pid]=1
        #print(cart)
        request.session['cart']=cart
        return redirect('/')
        
        
class Cart(View):
    def get(self,request):
        lst=list(request.session['cart'].keys())   
        products=Product.objects.filter(id__in = lst) 
        return render(request,'cart.html',{'products':products})

class CheckOut(View):
    def post(self,request):
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        lst=list(request.session.get('cart').keys())
        cart=request.session.get('cart')
        products=Product.objects.filter(id__in = lst) 
        customer=User.objects.get(id=request.user.id)
        #print(phone,address,cart,products,customer)
        
        for p in products:
            x=str(p.id)
            order=Order(product=p,
            customer=User(id=request.user.id),
            quantity=cart[x],
            price=p.price,
            address=address,
            phone_number=phone)
            order.save()
        
        request.session['cart']={}
        return redirect('/cart/')

class Order_Show(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        ords=Order.objects.filter(customer=User(id=request.user.id))
        return render(request,'order.html',{'ords':ords})



def sign_up(request):
    if(request.method=="POST"):
        fm=SignupForm(request.POST,request.FILES)
        if(fm.is_valid()):
            fm.save()
            messages.success(request,"your acount is successfully create !!!")
    else:
        fm=SignupForm()
    return render(request,'sign.html',{'form':fm})

def Login(request):
    return_url=None
    if not request.user.is_authenticated :
        if(request.method=='POST'):
            fm=loginform(request=request,data=request.POST)
            if(fm.is_valid()):
                uname=fm.cleaned_data['username']
                passw=fm.cleaned_data['password']
                user=authenticate(username=uname,password=passw)
                if user is not None:
                    login(request,user)
                    messages.success(request,"you are login !!!")
                    return redirect('/')
        else:
            fm=loginform()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/signup/')

def Logout(request):
    logout(request)
    return redirect('/log/')
