# Generated by Django 3.2.18 on 2023-07-30 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_auto_20230729_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenpropiedad',
            old_name='imagen',
            new_name='imagenes',
        ),
        migrations.RemoveField(
            model_name='imagenpropiedad',
            name='propiedad',
        ),
        migrations.AlterModelTable(
            name='tipoprovincia',
            table='tipo_provincia',
        ),
    ]