# Generated by Django 4.0.4 on 2022-06-18 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_obra_arq_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arquitecto',
            old_name='nombre_arqui',
            new_name='nombre_apellido_arqui',
        ),
        migrations.RemoveField(
            model_name='arquitecto',
            name='apellido_arqui',
        ),
    ]
