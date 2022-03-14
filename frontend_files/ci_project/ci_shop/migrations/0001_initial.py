# Generated by Django 4.0.3 on 2022-03-14 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ci_category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('wholesale_cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ci_category.category')),
            ],
        ),
    ]
