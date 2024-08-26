class Aluno():
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def exibir_info(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Nota: {self.nota}"

class Escola():
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_info(self):
        info = f"Escola: {self.nome}\nAlunos:\n"
        for aluno in self.alunos:
            info += f"  - {aluno.exibir_info()}\n"
        return info

aluno1 = Aluno(nome="Maria", matricula="12345", nota=9.0)
aluno2 = Aluno(nome="João", matricula="67890", nota=8.5)

escola = Escola(nome="UENF")
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)

print(escola.exibir_info())
