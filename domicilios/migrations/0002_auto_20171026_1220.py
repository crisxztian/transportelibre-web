# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domicilios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='apellidosc',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='clavec',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='emailc',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='nombresc',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='telefonoc',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='domiciliarios',
            old_name='apellidosd',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='domiciliarios',
            old_name='claved',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='domiciliarios',
            old_name='emaild',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='domiciliarios',
            old_name='nombresd',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='domiciliarios',
            old_name='telefonod',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='estadoc',
        ),
        migrations.RemoveField(
            model_name='domiciliarios',
            name='estadod',
        ),
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.CharField(choices=[(0, 'invalidado'), (1, 'validado')], default='invalidado', max_length=10),
        ),
        migrations.AddField(
            model_name='domiciliarios',
            name='estado',
            field=models.CharField(choices=[(0, 'invalidado'), (1, 'validado')], default='invalidado', max_length=10),
        ),
    ]
