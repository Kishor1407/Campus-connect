# Generated by Django 3.2.7 on 2022-01-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20220104_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
