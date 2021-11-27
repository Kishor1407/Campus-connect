from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .models import Product, Cartorder, CartOrderitems
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.db import IntegrityError
import json
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
    return render(request, 'shop/aboutUs.html')


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


def managecart(request):
    cartdata = {}
    cartdata[str(request.GET['id'])] = {
        'id': request.GET['id'],
        'qty': request.GET['qty'],
        'name': request.GET['name'],
        'price': int(request.GET['price']),
        'size': request.GET['size'],
        'image': request.GET['image']
    }
    if 'cart' in request.session:
        if str(request.GET['id']) in request.session['cart']:
            ca_rt = request.session['cart']
            ca_rt[str(request.GET['id'])]['qty'] = int(ca_rt[str(request.GET['id'])]['qty']) + 1
            ca_rt[str(request.GET['id'])]['size'] = ca_rt[str(request.GET['id'])]['size'] + "," + request.GET['size']
            ca_rt.update(ca_rt)
            request.session['cart'] = ca_rt
        else:
            ca_rt = request.session['cart']
            ca_rt.update(cartdata)
            request.session['cart'] = ca_rt
    else:
        request.session['cart'] = cartdata
    return JsonResponse({'data': request.session['cart']})


def cart(request):
    total = 0
    request.session.get('cart')
    if 'cart' in request.session:
        for p_id, item in request.session['cart'].items():
            total += int(item['qty']) * float(item['price'])
        return render(request, 'shop/Cart.html', {'data': request.session['cart'], 'total': total})
    else:
        return render(request, 'shop/Cart.html')


def delete_items(request):
    pid = str(request.GET['id'])
    if 'cart' in request.session:
        if pid in request.session['cart']:
            ca_rt = request.session['cart']
            del request.session['cart'][pid]
            request.session['cart'] = ca_rt
    total = 0
    for p_id, item in request.session['cart'].items():
        total += int(item['qty']) * float(item['price'])
    t = render_to_string('ajax/cart-list.html', {'data': request.session['cart'], 'total': total})
    return JsonResponse({'data': t})


def update_items(request):
    pid = str(request.GET['id'])
    value = request.GET['val']
    if 'cart' in request.session:
        if pid in request.session['cart']:
            ca_rt = request.session['cart']
            if value == 'minus':
                request.session['cart'][pid]['qty'] = max(0, (int(request.session['cart'][pid]['qty']) - 1))
            elif value == 'plus':
                request.session['cart'][pid]['qty'] = int(request.session['cart'][pid]['qty']) + 1
            if request.session['cart'][pid]['qty'] == 0:
                del request.session['cart'][pid]
            request.session['cart'] = ca_rt
    total = 0
    for p_id, item in request.session['cart'].items():
        total += int(item['qty']) * float(item['price'])
    t = render_to_string('ajax/cart-list.html', {'data': request.session['cart'], 'total': total})
    return JsonResponse({'data': t})


def checkout(request):
    if request.user.is_authenticated:
        total = 0
        for p_id, item in request.session['cart'].items():
            total += int(item['qty']) * float(item['price'])
        order = Cartorder.objects.create(
            user=request.user,
            total_amt=total
        )
        for p_id, item in request.session['cart'].items():
            total += int(item['qty']) * float(item['price'])
            items = CartOrderitems.objects.create(
                order=order,
                invoice_no='INV_'+str(order.id),
                item=item[]
            )
        return render(request, 'shop/checkout.html', {'total': total})
    else:
        messages.error(request, "Login required to place order")
        return redirect("/login")