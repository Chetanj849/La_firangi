# Generated by Django 2.0.5 on 2019-08-14 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_address',
            field=models.ForeignKey(default=None, on_delete='CASCADE', to='App.Checkout'),
        ),
    ]