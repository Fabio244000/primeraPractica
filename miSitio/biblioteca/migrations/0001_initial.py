# Generated by Django 3.2 on 2021-04-23 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('portada', models.ImageField(upload_to='portadas')),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.editor')),
            ],
        ),
    ]
