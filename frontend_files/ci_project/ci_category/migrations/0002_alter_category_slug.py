# Generated by Django 4.0.3 on 2022-03-14 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
