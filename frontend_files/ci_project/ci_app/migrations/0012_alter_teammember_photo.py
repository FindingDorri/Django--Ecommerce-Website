# Generated by Django 4.0.3 on 2022-03-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci_app', '0011_customerorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]