# Generated by Django 4.2.6 on 2023-10-26 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0003_remove_asignacion_disponibilidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='costo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cursos',
            name='horario',
            field=models.CharField(default='Sin horario', max_length=20),
        ),
    ]
