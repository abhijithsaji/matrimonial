# Generated by Django 3.2.2 on 2021-05-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_alter_customer_diet'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
