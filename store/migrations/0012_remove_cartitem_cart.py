# Generated by Django 5.0.1 on 2024-02-01 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cartitem_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]
