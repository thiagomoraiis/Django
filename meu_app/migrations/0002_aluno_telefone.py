# Generated by Django 4.1.4 on 2022-12-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(null=True),
        ),
    ]