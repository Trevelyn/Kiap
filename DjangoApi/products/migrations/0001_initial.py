# Generated by Django 3.1.3 on 2020-11-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=250)),
            ],
        ),
    ]
