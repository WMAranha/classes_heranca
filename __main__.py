from modules.pessoa import pessoa
from modules.funcionario import funcionario
from modules.aluno import aluno
from modules.aluno_portugues import aluno_portugues
from modules.aluno_matematica import aluno_matematica

if __name__ == '__main__':
    # Instanciando os 5 objetos da classe pessoa:
    pessoa1 = pessoa("Valdir", 236457, "Rua Floriano", "98664-5497")
    pessoa2 = pessoa("Henrique", 947585, "Rua Atlas", "93934-5092")
    pessoa3 = pessoa("Paulo", 198637, "Rua Damares", "98223-5129")
    pessoa4 = pessoa("Mariana", 194743, "Rua Florentina", "99276-0363")
    pessoa5 = pessoa("Paula", 684275, "Rua Navio", "90387-1943")

    # Print com as informações de todas as pessoas:
    print("\nINFORMAÇÕES DAS PESSOAS\n")
    pessoa1.print_pessoa(),print("\n")
    pessoa2.print_pessoa(),print("\n")
    pessoa3.print_pessoa(),print("\n")
    pessoa4.print_pessoa(),print("\n")
    pessoa5.print_pessoa()
    
    # Instanciando os 5 objetos da classe funcionário:
    clara = funcionario("Clara Martins", 986309,"Rua Marechal Dias", "97642-0998", 25, "Supervisor")
    pedro = funcionario("Pedro Barbosa", 927583,"Rua das Flores", "90373-4275", 45, "Analista")
    monique = funcionario("Monique Hipolito", 438602,"Rua Paineiras", "97642-8956", 37, "Gerente")
    eduardo = funcionario("Eduardo Brito", 285653,"Rua Moçambique", "97642-9633", 98, "Supervisor de operações")
    cintia = funcionario("Cíntia Platão", 83533,"Rua Pernambucana", "97642-8622", 12, "Administrativo")

    # Print com as informações de todos os funcionários:
    print("\nINFORMAÇÕES DOS FUNCIONÁRIOS\n")
    clara.print_funcionario(),print("\n")
    pedro.print_funcionario(),print("\n")
    monique.print_funcionario(),print("\n")
    eduardo.print_funcionario(),print("\n")
    cintia.print_funcionario()

    # Instanciando os 5 objetos da classe aluno:
    aluno1 = aluno("Luis Chaves",237836,"Avenida João Pessoa", "96382-2167", 215)
    aluno2 = aluno("Clara Machado",383649,"Avenida Carlos Dias", "96382-9463", 190)
    aluno3 = aluno("Alexandre Paiva",835634,"Avenida Paulo Frontin", "96382-8256", 130)
    aluno4 = aluno("Gisely Monteiro",286342,"Rua das Aráras", "96382-3836", 73)
    aluno5 = aluno("Fabrício Marques",784632,"Avenida Joaquim", "96382-9837", 282)
 
    # Print com as informações dos alunos:
    print("\nINFORMAÇÕES DOS ALUNOS\n")
    aluno1.print_aluno(),print("\n")
    aluno2.print_aluno(),print("\n")
    aluno3.print_aluno(),print("\n")
    aluno4.print_aluno(),print("\n")
    aluno5.print_aluno()

    # Instanciando os 5 objetos da classe aluno_portugues:
    joao = aluno_portugues("João Pereira da Silva", 264856, "Rua Prados", "96475-8243", 75, 8.0)
    gabriel = aluno_portugues("Gabriel Salvador", 836342, "Rua Moreira", "96475-2724", 82, 8.7)
    elisa = aluno_portugues("Elisa Cicaroli", 947634, "Rua das Cachaças", "96475-9463", 47, 6.5)
    joana = aluno_portugues("Joana Dark", 364854, "Rua Cantoreira", "96475-1233", 8, 4.0)
    marcos = aluno_portugues("Marcos Dantona", 735237, "Rua Alvarenga", "96475-8562", 102, 9.0)

    # Print de todos os alunos de português:
    print("\nINFORMAÇÕES DOS ALUNOS DE PORTUGUÊS\n")
    joao.print_aluno_portugues(),print("\n")
    gabriel.print_aluno_portugues(),print("\n")
    elisa.print_aluno_portugues(),print("\n")
    joana.print_aluno_portugues(),print("\n")
    marcos.print_aluno_portugues()

    # Instanciando os 5 objetos da classe aluno_matematica:
    matheus = aluno_matematica("Matheus Henrique", 867352, "Rua da Alameda", "97364-9474", 52, 7.5)
    carlos = aluno_matematica("Carlos Emanoel", 836474, "Rua das Garças", "97364-1927", 64, 7.9)
    pedro = aluno_matematica("Pedro Braga", 174398, "Rua da Pedra", "97364-9352", 17, 8.2)
    adriana = aluno_matematica("Adriana Calcanhoto", 683426, "Rua das Marés", "97364-0372", 94, 4.7)
    marcela = aluno_matematica("Marcela Guimarães", 724184, "Rua da Estrada", "97364-8363", 72, 5.5)

    # Print com as informações dos alunos de matemática:
    print("\nINFORMAÇÕES DOS ALUNOS DE MATEMÁTICA\n")
    matheus.print_aluno_matematica(),print("\n")
    carlos.print_aluno_matematica(),print("\n")
    pedro.print_aluno_matematica(),print("\n")
    adriana.print_aluno_matematica(),print("\n")
    marcela.print_aluno_matematica()

