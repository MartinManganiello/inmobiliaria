# Generated by Django 3.0.1 on 2019-12-19 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='province',
            field=models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], max_length=50),
        ),
    ]