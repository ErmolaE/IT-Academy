# Generated by Django 4.0 on 2021-12-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_employee_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='economic_stage',
            field=models.CharField(choices=[('c', 'concept'), ('r', 'r&d'), ('f', 'finished product')], max_length=1),
        ),
    ]
