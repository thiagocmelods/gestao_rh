# Generated by Django 4.1.5 on 2023-02-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrohoraextra',
            old_name='Funcionario',
            new_name='funcionario',
        ),
        migrations.AlterField(
            model_name='registrohoraextra',
            name='motivo',
            field=models.CharField(max_length=100),
        ),
    ]
