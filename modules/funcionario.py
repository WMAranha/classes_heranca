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
        try:
            print("Nome: ",self.nome)
            print("RG: ", self.rg)
            print("Endereço: ", self.endereco)
            print("Contato: ", self.contato)
            print("ID: ", self.id_funcionario)
            print("Cargo: ", self.cargo)
        except Exception as e:
            print("Erro: ", str(e))

    def set_id_funcionario (self, id_funcionario):
        try:
            self.id_funcionario = id_funcionario
        except Exception as e:
            print("Erro: ", str(e))

    def set_cargo (self, cargo):
        try:
            self.cargo = cargo
        except Exception as e:
            print("Erro: ", str(e))

    def get_id_funcionario(self):
        try:
            return self.id_funcionario
        except Exception as e:
            print("Erro: ", str(e))

    def get_cargo(self):
        try:
            return self.cargo
        except Exception as e:
            print("Erro: ", str(e))
