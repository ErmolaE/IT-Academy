# Generated by Django 4.0 on 2021-12-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_consumer_adress_alter_consumer_postcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
    ]
