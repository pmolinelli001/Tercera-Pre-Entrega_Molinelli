# Generated by Django 4.2.11 on 2024-03-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_casa_departamento_cuatro_ambientes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hogar',
            name='jardin',
        ),
    ]
