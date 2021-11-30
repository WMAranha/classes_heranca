from modules.pessoa import pessoa

class aluno (pessoa):

    matricula = 0

    def __init__(self, nome, rg, endereco, contato, matricula):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.matricula = matricula

    def print_aluno(self):
        print("Nome: ",self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Contato: ", self.contato)
        print("Matrícula: ", self.matricula)

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula
