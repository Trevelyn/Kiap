# Generated by Django 3.1.3 on 2021-01-15 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0004_products_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('quanity', models.IntegerField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('customerName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id', to='products.products')),
                ('productName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Name', to='products.products')),
            ],
        ),
    ]
