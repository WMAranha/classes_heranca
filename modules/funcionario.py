from modules.pessoa import pessoa

class funcionario (pessoa):
    # nome = ""
    # rg = 0
    # endereco = ""
    # contato = ""
    id_funcionario = 0
    cargo = ""


    def __init__(self, nome, rg, endereco, contato, id_funcionario, cargo):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato
        self.id_funcionario = id_funcionario
        self.cargo = cargo

    def print_funcionario(self):
        print("Nome: ",self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Contato: ", self.contato)
        print("ID: ", self.id_funcionario)
        print("Cargo: ", self.cargo)

    def set_id_funcionario (self, id_funcionario):
        self.id_funcionario = id_funcionario

    def set_cargo (self, cargo):
        self.cargo = cargo


    def get_id_funcionario(self):
        return self.id_funcionario

    def get_cargo(self):
        return self.cargo
