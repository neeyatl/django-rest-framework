# Generated by Django 4.0.4 on 2022-06-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customer_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.datasheet'),
        ),
    ]