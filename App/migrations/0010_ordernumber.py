# Generated by Django 2.0.5 on 2019-09-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_returnorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField(default=1)),
            ],
        ),
    ]