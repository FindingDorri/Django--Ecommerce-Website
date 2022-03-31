# Generated by Django 3.1.4 on 2022-03-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ci_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]