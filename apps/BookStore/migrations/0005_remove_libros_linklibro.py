# Generated by Django 2.0.6 on 2021-09-26 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0004_auto_20210925_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libros',
            name='linklibro',
        ),
    ]
