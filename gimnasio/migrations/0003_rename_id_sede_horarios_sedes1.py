# Generated by Django 3.2.7 on 2021-11-18 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasio', '0002_auto_20211118_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horarios',
            old_name='id_sede',
            new_name='sedes1',
        ),
    ]
