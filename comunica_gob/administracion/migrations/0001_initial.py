# Generated by Django 4.2.2 on 2023-06-28 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField(null=True)),
                ('colonia', models.CharField(max_length=100)),
                ('ciudad', models.CharField(default='Chihuahua', max_length=100)),
                ('email', models.CharField(max_length=100, null=True)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('estado', models.CharField(choices=[('', 'Seleccione'), ('AG', 'Aguascalientes'), ('BC', 'Baja California'), ('BS', 'Baja California Sur'), ('CM', 'Campeche'), ('CS', 'Chiapas'), ('CH', 'Chihuahua'), ('CO', 'Coahuila'), ('CL', 'Colima'), ('DF', 'Ciudad de México'), ('DG', 'Durango'), ('GT', 'Guanajuato'), ('GR', 'Guerrero'), ('HG', 'Hidalgo'), ('JA', 'Jalisco'), ('MX', 'México'), ('MI', 'Michoacán'), ('MO', 'Morelos'), ('NA', 'Nayarit'), ('NL', 'Nuevo León'), ('OA', 'Oaxaca'), ('PU', 'Puebla'), ('QT', 'Querétaro'), ('QR', 'Quintana Roo'), ('SL', 'San Luis Potosí'), ('SI', 'Sinaloa'), ('SO', 'Sonora'), ('TB', 'Tabasco'), ('TM', 'Tamaulipas'), ('TL', 'Tlaxcala'), ('VE', 'Veracruz'), ('YU', 'Yucatán'), ('ZA', 'Zacatecas')], default='1', max_length=100)),
                ('estatus', models.CharField(default='A', max_length=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField(null=True)),
                ('colonia', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('', 'Seleccione'), ('AG', 'Aguascalientes'), ('BC', 'Baja California'), ('BS', 'Baja California Sur'), ('CM', 'Campeche'), ('CS', 'Chiapas'), ('CH', 'Chihuahua'), ('CO', 'Coahuila'), ('CL', 'Colima'), ('DF', 'Ciudad de México'), ('DG', 'Durango'), ('GT', 'Guanajuato'), ('GR', 'Guerrero'), ('HG', 'Hidalgo'), ('JA', 'Jalisco'), ('MX', 'México'), ('MI', 'Michoacán'), ('MO', 'Morelos'), ('NA', 'Nayarit'), ('NL', 'Nuevo León'), ('OA', 'Oaxaca'), ('PU', 'Puebla'), ('QT', 'Querétaro'), ('QR', 'Quintana Roo'), ('SL', 'San Luis Potosí'), ('SI', 'Sinaloa'), ('SO', 'Sonora'), ('TB', 'Tabasco'), ('TM', 'Tamaulipas'), ('TL', 'Tlaxcala'), ('VE', 'Veracruz'), ('YU', 'Yucatán'), ('ZA', 'Zacatecas')], default='1', max_length=100)),
                ('ciudad', models.CharField(max_length=100, null=True)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('tipo_reporte', models.CharField(max_length=100)),
                ('estatus', models.CharField(default='A', max_length=1)),
                ('descripcion', models.CharField(max_length=250, null=True)),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.personas')),
            ],
        ),
    ]
