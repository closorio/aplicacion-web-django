# Generated by Django 4.2.5 on 2023-10-02 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0005_articulodeportivo_disponible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorMulta', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=False)),
                ('fechaMulta', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaPagoMulta', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
