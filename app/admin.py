from django.contrib import admin
from .models import *

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'instituicao')
    search_fields = ('aluno', 'curso', 'instituicao')

# class PessoaInline(admin.TabularInline):
#     model = Pessoa
#     extra = 1


# class OcupacaoAdmin(admin.ModelAdmin):
#     inlines = [PessoaInline]


# class OcupacaoInline(admin.TabularInline):
#     model = Ocupacao
#     extra = 1

# class PessoasAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
#     search_fields = ('nome', 'cpf', 'email', 'cidade', 'ocupacao')
#     inlines = [OcupacaoInline]

class CursoinLine(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade')
    inlines = [CursoinLine]

class Areas_SaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoinLine]


admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Ocupacao)
# admin.site.register(Pessoa)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Areas_Saber, Areas_SaberAdmin)
admin.site.register(Curso)
admin.site.register(Turno)
admin.site.register(Disciplina)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Tipo_Avaliacao)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Aluno)
