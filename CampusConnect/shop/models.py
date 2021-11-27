from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default=0)
    subcategory = models.CharField(max_length=50, default=0)
    size = models.JSONField(max_length=5, default=0)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    images = models.ImageField(upload_to="shop/images", default="")
    backimages = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amt = models.FloatField()
    item = models.CharField(max_length=150)
class Cartorder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amt = models.FloatField()
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)


class CartOrderitems(models.Model):
    order = models.ForeignKey(Cartorder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=150)
    item = models.CharField(max_length=150)
    image = models.CharField(max_length=300)
    qty = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()