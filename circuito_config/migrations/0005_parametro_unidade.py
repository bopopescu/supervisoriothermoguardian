# Generated by Django 2.2.6 on 2019-10-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuito_config', '0004_parametro_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='unidade',
            field=models.CharField(choices=[('bar', 'bar(g)'), ('celsius', '˚C'), ('segundos', 'segundos'), ('percentual', '%'), ('sem', 'sem unidade definida')], default='sem', max_length=20),
        ),
    ]
