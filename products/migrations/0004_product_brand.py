# Generated by Django 2.2.6 on 2020-08-13 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Brand'),
            preserve_default=False,
        ),
    ]
