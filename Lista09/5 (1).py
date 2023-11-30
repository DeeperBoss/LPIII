from datetime import datetime

class Aluno:
    def __init__(self, nome, matricula, data_admissao, semestre, tipo_curso):
        self.nome = nome
        self.matricula = matricula
        self.data_admissao = data_admissao
        self.semestre = semestre
        self.tipo_curso = tipo_curso

    def calcular_mensalidade(self):
        valor_base = 700
        if self.tipo_curso == 'Engenharias':
            valor_base += valor_base * 0.2
        elif self.tipo_curso == 'Computação':
            valor_base += valor_base * 0.1
        elif self.tipo_curso == 'Letras':
            valor_base += valor_base * 0.05

        meses_cursados = (datetime.now() - self.data_admissao).days // 30
        if meses_cursados != self.semestre:
            valor_base += valor_base * 0.2

        return valor_base

    def __str__(self):
        return f'Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.tipo_curso}, Mensalidade: {self.calcular_mensalidade()}'

class AlunoPosGraduacao(Aluno):
    def __init__(self, nome, matricula, data_admissao, semestre, tipo_curso, orientador, titulo_projeto, nivel):
        super().__init__(nome, matricula, data_admissao, semestre, tipo_curso)
        self.orientador = orientador
        self.titulo_projeto = titulo_projeto
        self.nivel = nivel

class AlunoMestrado(AlunoPosGraduacao):
    def calcular_mensalidade(self):
        valor_base = super().calcular_mensalidade()
        meses_cursados = (datetime.now() - self.data_admissao).days // 30
        if meses_cursados > 24:
            valor_base += valor_base * 0.2
        return valor_base

class AlunoDoutorado(AlunoPosGraduacao):
    def calcular_mensalidade(self):
        valor_base = super().calcular_mensalidade()
        meses_cursados = (datetime.now() - self.data_admissao).days // 30
        if meses_cursados > 48:
            valor_base += valor_base * 0.2
        return valor_base

# Programa de exemplo
aluno1 = Aluno('João', '123', datetime