# Generated by Django 2.1.7 on 2020-05-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200511_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimento',
            name='tipo_resultado',
            field=models.CharField(choices=[['1', 'Padrão'], ['2', 'Bera'], ['3', 'Pac'], ['4', 'Audiometria']], default='1', max_length=1),
        ),
    ]
