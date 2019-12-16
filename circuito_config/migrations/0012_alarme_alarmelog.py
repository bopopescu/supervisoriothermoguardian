# Generated by Django 2.2.6 on 2019-12-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circuito_config', '0011_superaquecimentolog_datahora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('no_slave', models.IntegerField()),
                ('no_parametro', models.IntegerField()),
                ('minimo', models.FloatField(default=0)),
                ('maximo', models.FloatField(default=0)),
                ('em_alarme', models.BooleanField(default=False)),
                ('ultimo_email_enviado', models.DateTimeField(blank=True, null=True)),
                ('ultimo_sms_enviado', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alarmelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('datahora', models.DateTimeField(auto_now_add=True)),
                ('email_enviado', models.BooleanField(default=False)),
                ('sms_enviado', models.BooleanField(default=False)),
                ('alarme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circuito_config.Alarme')),
            ],
        ),
    ]