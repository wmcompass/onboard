# Generated by Django 3.0.7 on 2020-08-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0015_purchase_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custid',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='customerID',
        ),
    ]