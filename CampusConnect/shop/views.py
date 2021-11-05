from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.db import IntegrityError
# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def tshirts(request):
    allProds = []
    catprods = Product.objects.values('subcategory', 'id')
    cats = {item["subcategory"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(subcategory=cat)
        n = len(prod)
        allProds.append([prod, range(n), n])
    params = {'allProds': allProds}

    return render(request, 'shop/tshirts.html', params)


def hoodies(request):
    allProds = []
    catprods = Product.objects.values('subcategory', 'id')
    cats = {item["subcategory"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(subcategory=cat)
        n = len(prod)
        allProds.append([prod, range(n), n])
    params = {'allProds': allProds}

    return render(request, 'shop/hoodies.html', params)


def productview(request, myid):
    prod = Product.objects.filter(id=myid)
    return render(request, 'shop/product.html', {'product': prod[0]})


def aboutus(request):
    return render(request, 'shop/aboutus.html')


def signup(request):
    return render(request, 'shop/signUp.html')


def handelsignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        number = request.POST['number']

        if len(password) < 8:
            messages.error(request, "Password should be greater than 8 digits")
            return redirect('/Signup')
        if len(number) != 10:
            messages.error(request, "enter a valid number")
            return redirect('/Signup')

        checkemail = User.objects.filter(email=email)
        if checkemail:
            messages.error(request, "e-mail already registered, please use a different id")
            return redirect('/Signup')


        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            messages.error(request, "Username already taken  please enter a unique Username")
            return redirect('/Signup')
        user.name = username
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

    else:
        return HttpResponse("404 - Not found")


def loginpage(request):
    return render(request, 'shop/login.html')


def handeLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/login")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    return redirect('/')


def cart(request):
    return render(request, 'shop/Cart.html')



