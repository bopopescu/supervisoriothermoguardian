# Generated by Django 2.2.6 on 2019-12-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuito_config', '0013_auto_20191216_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarme',
            name='tempo_para_reenvio_email',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='alarme',
            name='tempo_para_reenvio_sms',
            field=models.IntegerField(default=2),
        ),
    ]