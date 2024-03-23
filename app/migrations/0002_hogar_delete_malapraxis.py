# Generated by Django 4.2.11 on 2024-03-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hogar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metros_cubiertos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('año', models.IntegerField()),
                ('tipo_propiedad', models.CharField(max_length=30)),
                ('jardin', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='MalaPraxis',
        ),
    ]
