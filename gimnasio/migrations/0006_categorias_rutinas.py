# Generated by Django 3.2.7 on 2021-11-19 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gimnasio', '0005_auto_20211118_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rutinas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gimnasio.categorias')),
            ],
        ),
    ]
