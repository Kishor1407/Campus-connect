# Generated by Django 3.2.7 on 2021-12-04 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default=0, max_length=50)),
                ('subcategory', models.CharField(default=0, max_length=50)),
                ('size', models.JSONField(default=0, max_length=5)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
                ('backimages', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(default='none', max_length=500)),
                ('size', models.CharField(default='S', max_length=10)),
                ('qty', models.IntegerField(default=0)),
                ('Hostel_name', models.CharField(max_length=500)),
                ('Unit', models.CharField(max_length=4)),
                ('City', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
                ('landmark', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
