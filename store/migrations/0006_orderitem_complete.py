# Generated by Django 4.0.2 on 2022-03-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orderitem_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
