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
        try:
            print("Nome: ",self.nome)
            print("RG: ", self.rg)
            print("Endereço: ", self.endereco)
            print("Contato: ", self.contato)
            print("Matrícula: ", self.matricula)
        except Exception as e:
            print("Erro: ", str(e))

    def set_matricula(self, matricula):
        try:
            self.matricula = matricula
        except Exception as e:
            print("Erro: ", str(e))

    def get_matricula(self):
        try:
            return self.matricula
        except Exception as e:
            print("Erro: ", str(e))
