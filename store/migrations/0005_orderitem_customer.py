# Generated by Django 4.0.2 on 2022-03-31 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
    ]
