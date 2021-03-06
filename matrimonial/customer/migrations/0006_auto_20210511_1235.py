# Generated by Django 3.2.2 on 2021-05-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_caste'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='about_me',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='caste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.caste'),
        ),
        migrations.AddField(
            model_name='customer',
            name='college_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='college_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='company_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='course',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='education',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lan_number',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='mother_tongue',
            field=models.CharField(blank=True, choices=[('Malayalam', 'malayalam'), ('Hindi', 'hindi'), ('Tamil', 'Tamil'), ('English', 'english'), ('Other', 'other')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='physical_status',
            field=models.CharField(blank=True, choices=[('Healthy', 'healthy'), ('Mild', 'mild'), ('Rather Not To Say', 'rather not to say')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.religion'),
        ),
        migrations.AddField(
            model_name='customer',
            name='school_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='school_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='specification',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='year_of_passout_college',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='year_of_passout_school',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
