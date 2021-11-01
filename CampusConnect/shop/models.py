from django.db import models

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
