# Generated by Django 4.2.11 on 2024-03-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_vida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='codigo_postal',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='art',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=40),
        ),
        migrations.AlterField(
            model_name='auto',
            name='codigo_postal',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='vida',
            name='correo_electronico',
            field=models.EmailField(max_length=40),
        ),
    ]