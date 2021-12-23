# Generated by Django 4.0 on 2021-12-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_material_density_alter_material_molar_mass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='postcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='postcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
