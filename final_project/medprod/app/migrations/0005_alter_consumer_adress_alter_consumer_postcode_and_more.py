# Generated by Django 4.0 on 2021-12-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_description_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='adress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='postcode',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='site',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='material',
            name='density',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='material',
            name='molar_mass',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='adress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='postcode',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='site',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
