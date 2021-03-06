# Generated by Django 3.2.7 on 2021-11-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasio', '0003_rename_id_sede_horarios_sedes1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=32)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RenameField(
            model_name='horarios',
            old_name='sedes1',
            new_name='sedes',
        ),
        migrations.RemoveField(
            model_name='horarios',
            name='hora_fin',
        ),
        migrations.RemoveField(
            model_name='horarios',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='telefono',
        ),
    ]
