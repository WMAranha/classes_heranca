class pessoa():
    # Defini os atributos da classe pessoa:
    nome = ""
    rg = 0
    endereco = ""
    contato = ""

    # Defini o construtor:
    def __init__(self, nome, rg, endereco, contato):
        self.nome = nome
        self.rg = rg
        self.endereco = endereco
        self.contato = contato

    # Criei todos os setters:
    def print_pessoa(self):
        print("Nome: ",self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Contato: ", self.contato)

    def set_nome(self,nome):
        try:
            self.nome = nome
        except Exception as e:
            print("Erro: ", str(e))

    def set_rg(self,rg):
        try:
            self.rg = rg
        except Exception as e:
            print("Erro: ", str(e))
    
    def set_endereco(self,endereco):
        try:
            self.endereco = endereco
        except Exception as e:
            print("Erro: ", str(e))

    def set_contato(self,contato):
        try:
            self.contato = contato
        except Exception as e:
            print("Erro: ", str(e))

    # Crei todos os getters:
    def get_nome (self):
        try:
            return self.nome
        except Exception as e:
            print("Erro: ", str(e))
    
    def get_rg (self):
        try:
            return self.rg
        except Exception as e:
            print("Erro: ", str(e))

    def get_endereco (self):
        try:
            return self.endereco
        except Exception as e:
            print("Erro: ", str(e))

    def get_contato (self):
        try:
            return self.contato
        except Exception as e:
            print("Erro: ", str(e))


 
