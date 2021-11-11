from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("hoodies/", views.hoodies, name="hoodies"),
    path("tshirts/", views.tshirts, name="tshirts"),
    path("about Us/", views.aboutus, name="aboutus"),
    path("productview/<int:myid>", views.productview, name="productview"),
    path("Signup/", views.signup, name="signup"),
    path("handelsignup", views.handelsignup, name="handelsignup"),
    path("login/", views.loginpage, name="Login"),
    path('handellogin', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    path('cart/', views.cart, name="cart"),
    path('managecart/', views.managecart, name="managecart"),
    path('delete-from-cart/', views.delete_items, name="delete_items"),

]
