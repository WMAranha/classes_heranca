from modules.aluno import aluno

class aluno_portugues(aluno):

    nota_portugues = 0

    def __init__(self, nome, rg, endereco, contato, matricula, nota_portugues):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.matricula = matricula
        self.nota_portugues = nota_portugues

    def print_aluno_portugues(self):
        print("Nome: ",self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Contato: ", self.contato)
        print("Matrícula: ", self.matricula)
        print("Nota de Português: ", self.nota_portugues)

    def set_nota_portugues(self, nota_portugues):
        self.nota_portugues = nota_portugues

    def get_nota_portugues(self):
        return self.nota_portugues
