# Generated by Django 3.2.3 on 2021-06-12 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_company_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.type'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='white', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='product_date',
            field=models.DateField(auto_now=True),
        ),
    ]
