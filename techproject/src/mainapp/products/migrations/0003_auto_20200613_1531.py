# Generated by Django 3.0.7 on 2020-06-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200613_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('desserts', 'desserts'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
