# Generated by Django 2.1.7 on 2020-05-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200512_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='lif',
            name='numero_lif_atual',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
