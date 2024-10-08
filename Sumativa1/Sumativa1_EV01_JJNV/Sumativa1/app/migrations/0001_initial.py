# Generated by Django 5.1 on 2024-09-04 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id_trabajador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('licencia_conducir', models.BooleanField(default=False)),
                ('observaciones', models.TextField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departamento')),
            ],
        ),
    ]
