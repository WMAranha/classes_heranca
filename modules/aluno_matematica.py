from modules.aluno import aluno

class aluno_matematica (aluno):

    nota_matematica = 0

    def __init__(self, nome, rg, endereco, contato, matricula, nota_matematica):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.matricula = matricula
        self.nota_matematica = nota_matematica

    def print_aluno_matematica(self):
        print("Nome: ",self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Contato: ", self.contato)
        print("Matrícula: ", self.matricula)
        print("Nota de Matemática: ", self.nota_matematica)

    def set_nota_matematica(self,nota_matematica):
        self.nota_matematica = nota_matematica

    
    def get_nota_matematica(self):
        return self.nota_matematica
