
class Pessoa(object):
    def __init__(self, nome, cor, altura, peso):
        super(Pessoa, self).__init__()
        self.nome = nome
        self.cor = cor
        self.altura = altura
        self.peso = peso
    
    def setNome(self, nome):
        self.nome = nome

    def getInfoPessoa(self):
        print(self.nome, self.cor, self.altura, self.peso)
        

class Aluno(Pessoa):
    def __init__(self, nome, cor, altura, peso, curso, turma, matricula):
        super(Aluno, self).__init__(nome, cor, altura, peso)
        self.curso = curso
        self.turma = turma
        self.matricula = matricula
        
    def setCurso(self, curso):
        self.curso = curso

    def getInfoAluno(self):
        print(self.nome, self.cor, self.altura, self.peso, self.curso, self.turma, self.matricula)

pessoa1 = Pessoa('Juca', 'pardo', 1.75, 76)
pessoa1.getInfoPessoa()

aluno1 = Aluno('João', 'Pardo', 1.70, 76, 'TSI', '2º Período', 222)
aluno2 = Aluno('Amadeu', 'Branco', 1.80, 83, 'TSI', '1º Período', 333)
aluno1.getInfoAluno()
aluno2.getInfoAluno()

