# Generated by Django 3.0.5 on 2020-04-23 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('datos_adicionales', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('prioridad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('notas', models.CharField(blank=True, max_length=10000)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('presupuesto', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Cliente')),
                ('empleados', models.ManyToManyField(to='myApp.Empleado')),
                ('tareas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Tarea')),
            ],
        ),
    ]
