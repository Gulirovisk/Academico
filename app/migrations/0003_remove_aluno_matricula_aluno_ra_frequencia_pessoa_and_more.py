# Generated by Django 5.1.3 on 2024-11-19 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_frequencia_pessoa_remove_matricula_pessoa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='matricula',
        ),
        migrations.AddField(
            model_name='aluno',
            name='ra',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Registro Acadêmico'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.aluno', verbose_name='Aluno'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.aluno', verbose_name='Aluno'),
        ),
    ]
