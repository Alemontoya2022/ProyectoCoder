# Generated by Django 4.2.4 on 2023-09-10 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_curso_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='cursos',
        ),
    ]
