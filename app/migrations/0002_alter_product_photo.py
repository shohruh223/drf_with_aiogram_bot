# Generated by Django 4.1.7 on 2023-03-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(max_length=80),
        ),
    ]