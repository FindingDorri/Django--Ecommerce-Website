# Generated by Django 3.1.4 on 2022-03-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci_shop', '0002_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
