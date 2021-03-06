# Generated by Django 2.2.6 on 2019-10-15 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('patrimonio', models.CharField(blank=True, max_length=100, null=True)),
                ('no_slave', models.IntegerField()),
                ('porta', models.CharField(max_length=255)),
                ('baudrate', models.IntegerField()),
                ('parity', models.CharField(choices=[('N', 'None'), ('E', 'Even'), ('O', 'Odd'), ('M', 'Mark'), ('S', 'Space')], default='N', max_length=1)),
                ('bytesize', models.IntegerField()),
                ('stopbits', models.IntegerField()),
                ('timeout', models.IntegerField()),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circuito_config.Circuito')),
            ],
        ),
    ]
