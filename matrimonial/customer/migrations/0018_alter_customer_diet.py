# Generated by Django 3.2.2 on 2021-05-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20210518_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='diet',
            field=models.CharField(choices=[('any', 'Any'), ('vegitarian', 'Vegiterian'), ('eggetarian', 'Eggetarian'), ('nonvegiterian', 'NonVegiterian')], default='any', max_length=20, null=True),
        ),
    ]
