# Generated by Django 5.1.2 on 2024-10-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_vehiculo_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(max_length=50),
        ),
    ]