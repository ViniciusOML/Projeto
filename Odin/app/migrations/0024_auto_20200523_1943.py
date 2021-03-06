# Generated by Django 2.1.15 on 2020-05-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200512_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cid', models.CharField(max_length=15)),
                ('nome_cid', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='lif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Lif'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Paciente'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Atendimento'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='procedimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Procedimento'),
        ),
        migrations.AlterField(
            model_name='resultadoaudiometria',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Consulta'),
        ),
        migrations.AlterField(
            model_name='resultadobera',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Consulta'),
        ),
        migrations.AlterField(
            model_name='resultadopac',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Consulta'),
        ),
        migrations.AlterField(
            model_name='resultadopadrao',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Consulta'),
        ),
        migrations.AddField(
            model_name='resultadoaudiometria',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Cid'),
        ),
        migrations.AddField(
            model_name='resultadobera',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Cid'),
        ),
        migrations.AddField(
            model_name='resultadopac',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Cid'),
        ),
        migrations.AddField(
            model_name='resultadopadrao',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Cid'),
        ),
    ]
