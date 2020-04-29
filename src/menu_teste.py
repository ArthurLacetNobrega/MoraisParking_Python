from estacionamento import Estacionamento
from datetime import datetime

estacionamento = Estacionamento()

data_atual = datetime.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

#usuario teste: (usuario: arthur senha: voltas28)
estacionamento.cadastrar_usuario('Arthur', '01233265748', 'gestor', 'Gerência', 'arthur', 'voltas28')

def login():
    print("^*^*^*^*^ MORAIS' PARKING SYSTEM ^*^*^*^*")
    print('=============== BEM VINDO ===============')
    print('        João Pessoa, ', data_em_texto)
    print('')

    print('================= LOGIN =================')
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if estacionamento.login(usuario, senha):
        principal()
    else:
        print("Usuário ou senha inválido! Tente novamente!\n\n")
        login()

def menu(titulo, opcoes):
    while True:
        print('')
        print("=" * 42)
        tam = int(42 - len(titulo))/2
        print(' ' * int(tam), titulo)
        print("=" * 42)
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("{%d} - %s" %(i, opcao))
        print("{%d} - Retornar/Sair" %(i+1))
        op = input("Opção: ")
        if op.isdigit():
            if int(op) == i + 1:
                # Encerra este menu e retorna a função anterior
                break
            if int(op) <= len(opcoes):
                # Chama a função do menu:
                opcoes[int(op) - 1][1]()
                continue
        print("Opção inválida. \n\n")

def principal():
    opcoes = [
        ("Veículos", menu_veiculos),
        ("Ocorrências", menu_ocorrencias)
    ]
    return menu("Morais' Parking", opcoes)

def menu_veiculos():
    opcoes = [
        ("Cadastrar Veículos", cadastrar_veiculo),
        ("Consultar Veículos", consultar_veiculo)

    ]
    return menu("Veículos", opcoes)

def menu_ocorrencias():
    opcoes = [
        ("Cadastrar Ocorrência", cadastrar_ocorrencia)
    ]
    return menu("OcorrÊncias", opcoes)

def cadastrar_veiculo():
    print('*********** CADASTRAR VEÍCULO ************')
    estacionamento.cadastrar_veiculo(input('Nome: '), input('Matícula: '), input('Curso: '), input('Placa: '),
                                     input('Modelo: '), input('Categoria: '))

def consultar_veiculo():
    print('*********** CONSULTAR VEÍCULO ************')
    veiculo = estacionamento.validar_veiculo(input('Placa: '))
    for veiculo in estacionamento.cadastro_veiculos:
        print(veiculo)

def cadastrar_ocorrencia():
    estacionamento.cadastrar_ocorrencia(int(input('ID: ')), input("Tipo: "), int(input('Quantidade de Veículos: ')),
                                        input('Data: '), input('Hora: '), input('Fatos: '))

login()