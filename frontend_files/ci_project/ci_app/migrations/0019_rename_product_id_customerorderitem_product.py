# Generated by Django 4.0.3 on 2022-03-10 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ci_app', '0018_rename_date_customerorder_date_ordered_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorderitem',
            old_name='product_id',
            new_name='product',
        ),
    ]