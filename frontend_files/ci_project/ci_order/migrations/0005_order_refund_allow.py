# Generated by Django 4.0.3 on 2022-04-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci_order', '0004_remove_refund_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='refund_allow',
            field=models.BooleanField(default=True),
        ),
    ]
