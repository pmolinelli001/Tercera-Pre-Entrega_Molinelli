# Generated by Django 4.2.11 on 2024-03-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_profesionales_dependiente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoberturaParcial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=50)),
                ('responsabilidad_civil', models.CharField(max_length=10)),
                ('reposicion_0km', models.CharField(max_length=10)),
                ('daño_incendio_robototal', models.CharField(max_length=10)),
                ('daño_parcial_por_robo', models.CharField(max_length=10)),
                ('cerraduras', models.CharField(max_length=10)),
                ('cristales_laterales', models.CharField(max_length=10)),
                ('daños_por_granizo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TodoRiesgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=50)),
                ('responsabilidad_civil', models.CharField(max_length=10)),
                ('reposicion_0km', models.CharField(max_length=10)),
                ('daño_incendio_robototal', models.CharField(max_length=10)),
                ('daño_parcial_por_robo', models.CharField(max_length=10)),
                ('cerraduras', models.CharField(max_length=10)),
                ('cristales_laterales', models.CharField(max_length=10)),
                ('daños_por_granizo', models.CharField(max_length=10)),
            ],
        ),
    ]