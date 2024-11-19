# Generated by Django 5.1.3 on 2024-11-19 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas_Saber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Area de Saber',
                'verbose_name_plural': 'Areas de Saber',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ocupacao',
                'verbose_name_plural': 'Ocupacoes',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Avaliacao',
                'verbose_name_plural': 'Tipos de Avaliacao',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2, unique=True)),
            ],
            options={
                'verbose_name': 'Unidade Federativa',
                'verbose_name_plural': 'Unidades Federativas',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areas_saber', verbose_name='Area de Saber')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('site', models.URLField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Instituicao',
                'verbose_name_plural': 'Instituicoes',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('carga_horaria_total', models.PositiveIntegerField()),
                ('duracao_meses', models.PositiveSmallIntegerField()),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areas_saber', verbose_name='Area de Saber')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao', verbose_name='Instituicao')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_pai', models.CharField(max_length=100)),
                ('nome_mae', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField(blank=True, default='2000-01-01', null=True, verbose_name='Data de Nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao', verbose_name='Ocupacao')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, default='2000-01-01', null=True, verbose_name='Data de Inicio')),
                ('data_previsao_termino', models.DateField(blank=True, default='2000-01-01', null=True, verbose_name='Data Previsao de Termino')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao', verbose_name='Instituicao')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
            },
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.PositiveSmallIntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Frequencia',
                'verbose_name_plural': 'Frequencias',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Nota')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('tipo_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_avaliacao', verbose_name='Tipo de Avaliacao')),
            ],
            options={
                'verbose_name': 'Avaliacao',
                'verbose_name_plural': 'Avaliacoes',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turno', verbose_name='Turno')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uf', verbose_name='Unidade Federativa'),
        ),
    ]
