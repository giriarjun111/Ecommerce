# Generated by Django 4.0.2 on 2022-03-31 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orderitem_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_ordered',
        ),
    ]
