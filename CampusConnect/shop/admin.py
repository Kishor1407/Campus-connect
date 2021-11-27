from django.contrib import admin

# Register your models here.
from.models import Product
from.models import Cartorder
from.models import CartOrderitems
admin.site.register(Product)
admin.site.regiser(Cartorder)
admin.site.regiser(CartOrderitems)
