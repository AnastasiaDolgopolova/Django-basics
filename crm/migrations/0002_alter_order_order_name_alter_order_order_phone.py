# Generated by Django 4.1.3 on 2022-12-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_phone',
            field=models.CharField(max_length=200, verbose_name='Phone'),
        ),
    ]
