from estacionamento import Estacionamento
from datetime import datetime

import getpass


estacionamento = Estacionamento()

data_atual = datetime.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')


def upload_bd():
    estacionamento.armazenar_veiculos()
    estacionamento.armazenar_proprietarios()
    estacionamento.armazenar_areas()
    estacionamento.armazenar_usuarios()
    estacionamento.armazenar_ocorrencias()

def login():
    upload_bd()

    print("^*^*^*^*^ MORAIS' PARKING SYSTEM ^*^*^*^*")
    print('=============== BEM VINDO ===============')
    print('        João Pessoa, ', data_em_texto)
    print('')

    print('================= LOGIN =================')
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    #senha = getpass.getpass(prompt='Senha: ', stream=None) #não funciona no pycharm, mas no prompt

    if estacionamento.login(usuario, senha):
        user = estacionamento.validar_usuario(usuario)
        if user.get_funcao() == 'GESTOR':
            principal_gestor()
        elif user.get_funcao() == 'RH':
            principal_rh()
        else:
            principal_func_est()
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
        escolha = input("Opção: ")
        if escolha.isdigit():
            if int(escolha) == i + 1:
                #é a seleção de retornar/sair
                break
            if int(escolha) <= len(opcoes):
                # Chama a função do menu:
                opcoes[int(escolha) - 1][1]() #esse parentese nofinal faz com que a funcao só rode após a apresentação do menu e escolha
                continue
        print("Opção inválida. Escolha novamente! \n\n")

def principal_gestor():
    opcoes = [
        ("Veículos", menu_veiculos),
        ("Controle de Acessos", menu_acessos),
        ("Ocorrências", menu_ocorrencias),
        ("Áreas", menu_areas),
    ]
    return menu("Morais' Parking", opcoes)

def principal_rh():
    opcoes = [
        ("Veículos", menu_veiculos),
        ("Controle de Acessos", menu_acessos),
        ("Ocorrências", menu_ocorrencias),
        ("Áreas", menu_areas),
    ]
    return menu("Morais' Parking", opcoes)

def principal_func_est():
    opcoes = [
        ("Veículos", menu_veiculos),
        ("Controle de Acessos", menu_acessos),
        ("Ocorrências", menu_ocorrencias),
        ("Áreas", menu_areas),
    ]
    return menu("Morais' Parking", opcoes)

def menu_veiculos():
    opcoes = [
        ("Cadastrar Veículos", cadastrar_veiculo),
        ("Consultar Veículos", consultar_veiculo),
        ("Remover Veículo", remover_veiculo),
        ("Consultar Proprietário", consultar_proprietario)
    ]

    return menu("Veículos", opcoes)

def cadastrar_veiculo():
    print('*********** CADASTRAR VEÍCULO ************')
    estacionamento.cadastrar_veiculo(input('Nome: '), input('Matícula: '), input('Curso: '), input('Placa: '),
                                     input('Modelo: '), input('Categoria: '))

def consultar_veiculo():
    print('*********** CONSULTAR VEÍCULO ************')
    estacionamento.consultar_veiculo(input('Placa: '))

def remover_veiculo():
    print('************ REMOVER VEÍCULO *************')
    estacionamento.remover_veiculo(input('Placa: '))

def consultar_proprietario():
    print('************ CONSULTAR PROPRIETARIO *************')
    estacionamento.consultar_proprietario(input('Placa: '))

def menu_acessos():
    opcoes = [
        ("Registrar Entrada", registrar_entrada),
        ("Registrar Saída", registrar_saida),
        ("Verificar Ocupacao", verificar_ocupacao),
    ]
    return menu("Controle de Acessos", opcoes)

def registrar_entrada():
    print('************ REGISTRAR ENTRADA *************')
    estacionamento.validar_entrada(input('Placa: '))

def registrar_saida():
    print('************ REGISTRAR SAIDA *************')
    estacionamento.validar_saida(input('Placa: '))

def verificar_ocupacao():
    print('************ CONSULTAR OCUPAÇÃO *************')
    print("Informe qual destas categorias desejas consultar a ocupação: ", estacionamento.get_categorias())
    categoria = input('Categoria: ')
    percent = estacionamento.ocupacao_areas(categoria)
    return print("A ocupação da categoria %s é %s porcento" % (categoria.upper(), percent))

def menu_ocorrencias():
    opcoes = [
        ("Cadastrar Ocorrência", cadastrar_ocorrencia),
        ("Consultar Ocorrência", menu_consulta_ocorrencia)
    ]
    return menu("Ocorrências", opcoes)

def cadastrar_ocorrencia():
    print('************ CADASTRAR OCORRENCIA *************')
    print('Lembrete: os tipos de ocorrência devem ser: ', estacionamento.tipo_ocorrencias)
    ocorrencia = estacionamento.cadastrar_ocorrencia(input("Tipo: "), int(input('Quantidade de Veículos: ')),
                                        input('Data: '), input('Hora: '), input('Fatos: '))

def menu_consulta_ocorrencia():
    opcoes = [
        ("Consultar por ID", consultar_ocorrencia_id),
        ("Consultar por Placa", consultar_ocorrencia_placa)

    ]
    return menu("Consultar Ocorrência", opcoes)

def consultar_ocorrencia_id():
    print('************ CONSULTAR OCORRENCIA *************')
    estacionamento.consultar_ocorrencia_id(int(input('ID: ')))

def consultar_ocorrencia_placa():
    print('************ CONSULTAR OCORRENCIA *************')
    estacionamento.consultar_ocorrencia_placa(input('Placa: '))

def menu_areas():
    opcoes = [
        ("Cadastrar Área", cadastrar_area),
        ("Consultar Área", consultar_area),
        ("Excluir Área", excluir_area),
        ("Status", verificar_status)

    ]
    return menu("Áreas", opcoes)

def cadastrar_area():
    print('************ CADASTRAR ÁREA *************')
    estacionamento.cadastrar_area(input('Nome: '), int(input('Capacidade: ')), input('Categoria: '))

def verificar_status():
    print('************ CONSULTAR STATUS *************')
    estacionamento.status_areas(input('Categoria Área: '))

def consultar_area():
    print('************ CONSULTAR ÁREA *************')
    print("Informe qual destas categorias desejas consultar: ", estacionamento.get_categorias())
    estacionamento.consultar_area(input("Área: "))

def excluir_area():
    print('************ EXCLUIR ÁREA *************')
    print("Informe qual destas áreas desejas excluir: ", estacionamento.get_categorias())
    estacionamento.excluir_area(input('Área: '))


login()