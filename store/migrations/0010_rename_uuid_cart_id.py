# Generated by Django 5.0.1 on 2024-01-31 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_remove_cart_id_alter_cart_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uuid',
            new_name='id',
        ),
    ]
