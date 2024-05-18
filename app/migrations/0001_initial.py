# Generated by Django 4.2.13 on 2024-05-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(blank=True, max_length=10, null=True)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estudiante_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante', verbose_name='Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
                ('estudiante_id', models.ManyToManyField(related_name='cursos', to='app.estudiante', verbose_name='Estudiante')),
                ('profesor_id', models.ManyToManyField(related_name='cursos', to='app.profesor', verbose_name='Profesor')),
            ],
        ),
    ]
