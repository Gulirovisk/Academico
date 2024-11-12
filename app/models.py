from django.db import models

class UF(models.Model):
    uf = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federativas'
    
    def __str__(self):
        return self.uf

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name='Unidade Federativa')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    
    def __str__(self):
        return f'{self.nome} - {self.uf}'
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ocupacao'
        verbose_name_plural = 'Ocupacoes'
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento', default='2000-01-01')
    email = models.EmailField(unique=True, blank= True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade')
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name='Ocupacao')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return f'{self.nome} - {self.cidade} - {self.ocupacao}'
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100, unique= True)
    site = models.URLField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade', blank=True, null=True)

    class Meta:
        verbose_name = 'Instituicao'
        verbose_name_plural = 'Instituicoes'

    def __str__(self):
        return f'{self.nome} - {self.cidade}'

class Areas_Saber(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Area de Saber'
        verbose_name_plural = 'Areas de Saber'

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveSmallIntegerField()
    area_saber = models.ForeignKey(Areas_Saber, on_delete=models.CASCADE, verbose_name='Area de Saber')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituicao')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f'{self.nome} - {self.area_saber} - {self.instituicao}'
    
class Turno(models.Model):
    nome = models.CharField(max_length=100) # Matutino, vespertino, noturno

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(Areas_Saber, on_delete=models.CASCADE, verbose_name='Area de Saber')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome
    
class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituicao')
    data_inicio = models.DateField(blank=True, null=True, verbose_name='Data de Inicio', default= '2000-01-01')
    data_previsao_termino = models.DateField(blank=True, null=True, verbose_name='Data Previsao de Termino', default= '2000-01-01')

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'

    def __str__(self):
        return f'{self.pessoa} - {self.curso} - {self.instituicao}'
    
class Tipo_Avaliacao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tipo de Avaliacao'
        verbose_name_plural = 'Tipos de Avaliacao'

    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    nota = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, verbose_name='Nota')
    tipo_avaliacao = models.ForeignKey(Tipo_Avaliacao, on_delete=models.CASCADE, verbose_name='Tipo de Avaliacao')

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'

    def __str__(self):
        return f'{self.descricao} - {self.curso} - {self.disciplina} - {self.tipo_avaliacao}'
    
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina  = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    numero_faltas = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Frequencia'
        verbose_name_plural = 'Frequencias'

    def __str__(self):
        return f'{self.pessoa} - {self.curso} - {self.disciplina}'
    
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    
    def __str__(self):
        return self.nome

    




