from areas import Areas
from proprietario import Proprietario
from usuario import Usuario
from veiculo import Veiculo
from ocorrencias import Ocorrencia
from eventos import Eventos
from datetime import datetime, timedelta
import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()


class Estacionamento:
    """Representa o estacionamento e cotrola a integração dos métodos das classes"""

    def __init__(self):
        self.controle_areas = list()
        self.cadastro_veiculos = list()
        self.cadastro_ocorrencias = list()
        self.cadastro_proprietarios = {}
        self.categorias = ['PREFERENCIAL','FUNCIONARIOS', 'CARRO', 'MOTOCICLETA', 'VAN', 'ÔNIBUS', 'VISITANTES']
        self.tipo_ocorrencias = ['FURTO', 'SINISTRO', 'ESTACIONAMENTO INDEVIDO', 'AVARIA', 'INUNDAÇÃO', 'OUTROS']
        self.cadastro_usuario = list()
        self.lista_ocupacao = list()

        #Cria a tabela eventos
        Eventos.criar_tabela()
        #Não foi necessário o uso desta lista, mantida pra ficar no padrão do projeto
        self.lista_de_eventos = []

    #getters
    def get_controle_areas(self):
        return self.controle_areas

    def get_cadastro_veiculos(self):
        return self.cadastro_veiculos

    def get_cadastro_ocorrencias(self):
        return self.cadastro_ocorrencias

    def get_categorias(self):
        return self.categorias

    def get_tipo_ocorrencias(self):
        return self.tipo_ocorrencias

    def get_cadastro_usuario(self):
        return self.cadastro_usuario

    #METODOS RELACIONADOS A CATEGORIAS
    def adicionar_categoria(self, categoria):
        '''Caso o gestor precise incluir uma nova categoria no estacionamento'''
        self.categorias.append(categoria.upper())

    def validar_cetegoria(self, categoria):
        '''funcao de validação de categoria'''
        if categoria.upper() not in self.categorias:
            print("Categoria inválida! A categoria deve ser uma dessas opções:  ", self.categorias)
            categoria = input("Insira a categoria: ").upper()
            return categoria

    # METODOS RELACIONADOS A VEICULOS e PROPRIETARIOS
    def cadastrar_veiculo(self, nome, matricula, curso, placa, modelo, categoria):
        if self.validar_veiculo(placa.upper()) == None:
            #cadastra o proprietário no dicionario e no BD
            prop = Proprietario(nome.upper(), matricula.upper(), curso.upper())
            c.execute(
                'CREATE TABLE IF NOT EXISTS proprietarios(placa TEXT PRIMARY KEY, nome TEXT, matricula TEXT, curso TEXT)')
            c.execute('INSERT INTO proprietarios VALUES (?, ?, ?,?)',
                      (placa.upper(), prop.get_nome(), prop.get_matricula(), prop.get_curso()))
            con.commit()
            self.armazenar_proprietarios()

            #Cadastra o veiculo no dicionario e no array
            veic = Veiculo(placa.upper(),prop.get_nome(), modelo.upper(), categoria.upper())
            c.execute(
                'CREATE TABLE IF NOT EXISTS veiculos(placa TEXT PRIMARY KEY, proprietario TEXT, modelo TEXT, categoria TEXT)')
            c.execute('INSERT INTO veiculos VALUES (?, ?, ?,?)', (veic.get_placa(), prop.get_nome(), veic.get_modelo(), veic.get_categoria()))
            con.commit()
            self.armazenar_veiculos()
        else:
            print('Veículo já está cadastrado!')
            resposta = input('Deseja cadastrá-lo novamente? (S/N) ')
            if resposta.upper() == 'S':
                self.remover_veiculo(placa.upper())
                self.cadastrar_veiculo(input('Nome: '), input('Matícula: '), input('Curso: '), input('Placa: '),
                                     input('Modelo: '), input('Categoria: '))


    def consultar_proprietario(self, placa):
        placa_busca = placa.upper()
        if placa_busca in self.cadastro_proprietarios.keys():
           print(self.cadastro_proprietarios[placa_busca])
        else:
            print("ATENÇÃO!!! Veículo não cadastrado!")

    def consultar_veiculo(self, placa):
        veiculo = self.validar_veiculo(placa.upper())
        if veiculo in self.get_cadastro_veiculos():
            print(veiculo)

    def validar_veiculo(self, placa):
        for veiculo in self.cadastro_veiculos:
            if placa.upper() == veiculo.get_placa():
                return veiculo
        return None

    def remover_veiculo(self, placa):
        #remove da base de dados
        c.execute("DELETE FROM veiculos WHERE placa = ?", (placa.upper(),))
        con.commit()
        c.execute("DELETE FROM proprietarios WHERE placa = ?", (placa.upper(),))
        con.commit()

        #remove da lista
        veiculo = self.validar_veiculo(placa.upper())
        self.cadastro_veiculos.remove(veiculo)

    def validar_entrada(self, placa):
        data_atual = datetime.today()
        data_em_texto = data_atual.strftime('%d/%m/%Y')
        hora_em_texto = data_atual.strftime('%H:%M')
        if self.validar_veiculo(placa.upper()) != None:
            veic = self.validar_veiculo(placa.upper())
            for area in self.get_controle_areas():
                if area.get_categoria().upper() == veic.get_categoria().upper():
                    area.entrada_veiculo(veic)
            c.execute(
                'CREATE TABLE IF NOT EXISTS entradas(data TEXT, hora TEXT,placa TEXT,categoria TEXT)')
            c.execute('INSERT INTO entradas VALUES (?,?,?,?)',
                      (data_em_texto, hora_em_texto, veic.get_placa().upper(), veic.get_categoria()))
            con.commit()
            self.lista_ocupacao.append(veic.get_placa())
            print('Entrada Registrada!')
        else:
            print('ATENÇÃO! Veículo não cadastrado!')
            resposta = input('Deseja permitir entrada como Visitante? (S/N) ')
            if resposta.upper() == "S":
                self.cadastrar_veiculo('Visitante', 'n/a', 'n/a', placa.upper(),
                                     'n/a', 'VISITANTES')
                self.validar_entrada(placa)
            else:
                return

    def validar_saida(self, placa):
        data_atual = datetime.today()
        data_em_texto = data_atual.strftime('%d/%m/%Y')
        hora_em_texto = data_atual.strftime('%H:%M')
        if placa.upper() in self.lista_ocupacao:
            veic = self.validar_veiculo(placa.upper())
            c.execute(
                'CREATE TABLE IF NOT EXISTS saidas(data TEXT, hora TEXT,placa TEXT,categoria TEXT)')
            c.execute('INSERT INTO saidas VALUES (?,?,?,?)',
                      (data_em_texto, hora_em_texto, veic.get_placa().upper(), veic.get_categoria()))
            con.commit()
            for area in self.get_controle_areas():
                if area.get_categoria().upper() == veic.get_categoria().upper():
                    area.saida_veiculo(veic)
            self.lista_ocupacao.remove(placa.upper())
            if veic.get_categoria() == 'VISITANTES':
                self.remover_veiculo(placa.upper())
            print('Saída Registrada!')
        else:
            print("Entrada não registrada!")

    # METODOS RELACIONADOS A ÁREAS
    def cadastrar_area(self, nome, capacidade, categoria):
        '''O usuário cadastra as áreas, de acordo com as categorias pré-definidas'''
        area = Areas(nome.upper(), capacidade, categoria.upper())

        #inserção no banco
        c.execute(
            'CREATE TABLE IF NOT EXISTS areas(nome TEXT, capacidade INT, categoria TEXT)')
        c.execute('INSERT INTO areas VALUES (?, ?, ?)',
                  (area.get_nome(), area.get_capacidade(), area.get_categoria()))
        con.commit()
        self.armazenar_areas()

    def consultar_area(self, categoria):
        categ_areas = {}
        for area in self.controle_areas:
            if categoria.upper() == area.get_categoria():
                categ_areas[area.get_nome()] = area.get_capacidade()

        if len(categ_areas) > 0:
            return categ_areas
        else:
            return "A categoria não possui área específica!"

    def alterar_capacidade(self, categoria, vagas):
        '''Método será utilizado nos dias de evento, onde a capacidade da área identificada será reduzida'''
        #alteração da capacidade no objeto Area
        for area in self.controle_areas:
            if categoria.upper() == area.get_categoria():
                nova_capacidade = area.get_capacidade() - vagas
                area.set_capacidade(nova_capacidade)

                # alteração da capacidade no Banco
                c.execute('UPDATE areas SET capacidade = ? WHERE categoria = ?',(nova_capacidade, categoria.upper()))
                con.commit()
            else:
                print('Área não cadastrada!')


    def excluir_area(self, categoria):
        '''Método utilizado pelo gestor, caso ele queira remover alguma área'''
        for area in self.controle_areas:
            if categoria.upper() == area.get_categoria():
                self.controle_areas.remove(categoria.upper())

                #exclusão do Banco
                c.execute('DELETE FROM areas WHERE categoria = ?', (categoria.upper()),)
                con.commit()
            else:
                print('Área não cadastrada!')

    def ocupacao_areas(self, categoria):
        '''Mostra o percentual de ocupação da área'''
        percent = 0
        ocup_total = 0
        for area in self.controle_areas:
            if categoria.upper() == area.get_categoria():
                quantidade = len(area.get_veiculos_area())
                ocup_total += quantidade
                percent = (ocup_total * 100 / area.get_capacidade())
        return percent

    def status_areas(self, categoria):
        '''Mostra os veículos que estão em cada área, naquele instante'''
        for area in self.controle_areas:
            if categoria.upper() == area.get_categoria():
                for veiculo in area.get_veiculos_area():
                    print(veiculo)

    #METODOS RELACIONADOS A USUARIOS
    def cadastrar_usuario(self,nome, cpf, funcao, setor, usuario, senha):
        user = Usuario(nome.upper(), cpf.upper(), funcao.upper(), setor.upper(), usuario, senha)
        c.execute(
            'CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, cpf TEXT, funcao TEXT, setor TEXT, usuario TEXT, senha TEXT)')
        c.execute('INSERT INTO usuarios VALUES (?, ?, ?, ?, ?, ?)',
                  (user.get_nome(), user.get_cpf(), user.get_funcao(), user.get_setor(), user.get_usuario(), user.get_senha()))
        con.commit()
        self.armazenar_usuarios()

    def validar_usuario(self, user):
        for usuario in self.cadastro_usuario:
            if user == usuario.get_usuario():
                return usuario
        return None

    def login(self, usuario, senha):
        user = self.validar_usuario(usuario)
        if user != None:
            if user.get_usuario() == usuario and user.get_senha() == senha:
                return True
            else:
                return False
        else:
            return False

    #METODOS RELACIONADOS A OCORRÊNCIAS
    def validar_tipo_ocorrencia(self):
        pass

    def cadastrar_ocorrencia(self, tipo, quantidade_veiculos, data, hora, fatos):
        id = len(self.cadastro_ocorrencias) + 1
        ocorrencia = Ocorrencia(id, tipo.upper(), quantidade_veiculos, data, hora, fatos)
        c.execute(
            'CREATE TABLE IF NOT EXISTS ocorrencias (id INTEGER, tipo TEXT, quantidade_veiculos INTEGER, data TEXT, hora TEXT, fatos TEXT)')
        c.execute('INSERT INTO ocorrencias VALUES (?, ?, ?, ?, ?, ?)',
                  (id, ocorrencia.get_tipo(), ocorrencia.get_quantidade_veiculos(), ocorrencia.get_data(), ocorrencia.get_hora(),
                   ocorrencia.get_fatos()))
        con.commit()
        for i in range(quantidade_veiculos):
            placa = input("Insira a placa do veículo %sº envolvido: "%(i+1))
            veiculo = self.validar_veiculo(placa.upper())
            if veiculo != None:
                c.execute(
                    'CREATE TABLE IF NOT EXISTS veiculos_ocorrencias (id INTEGER, placa TEXT)')
                c.execute('INSERT INTO veiculos_ocorrencias VALUES (?,?)', (ocorrencia.get_id(), veiculo.get_placa()))
                con.commit()
            else:
                print("Veículo não cadastrado!")
        print('Para acompanhamento, o ID desta ocorrência é: ', id)
        self.armazenar_ocorrencias()


    def consultar_ocorrencia_id(self, id):
        for ocorrencia in self.get_cadastro_ocorrencias():
            if id == ocorrencia.get_id():
                print(ocorrencia)
            else:
                print('Ocorrência não localizada!')

    def consultar_ocorrencia_placa(self, placa):
        c.execute("SELECT * FROM veiculos_ocorrencias WHERE placa = ?", (placa.upper(),))
        for linha in c.fetchall():
            id = linha[0]
            c.execute("SELECT * FROM ocorrencias WHERE id = ?", (id,))
            for linha in c.fetchall():
                print(linha)


     # MÉTODOS ARMAZENAMENTO - QUE REINSEREM NAS LISTAS, DICIONÁRIOS, OS VALORES JÁ REGISTRADOS

    '''Carrega os dados da tabela cadastro_eventos na lista (lista_de_eventos),
        que é um dos atributos da classe Estacionamento'''
    #Função desnecessário pois os dados já estão armazenados no banco de dados
    #havendo necessidade se faz uma busca
    # Não foi necessário o uso desta função, mantida pra ficar no padrão do projeto
    def armazenar_eventos(self):
        for tupla_evento in Eventos.all():
            self.lista_de_eventos.append(tupla_evento)

    def armazenar_veiculos(self):
        c.execute("SELECT * FROM veiculos ")
        for linha in c.fetchall():
            placa = linha[0]
            proprietario = linha[1]
            modelo = linha[2]
            categoria = linha[3]
            veiculo = Veiculo(placa, proprietario, modelo, categoria)
            self.cadastro_veiculos.append(veiculo)

    def armazenar_proprietarios(self):
        c.execute("SELECT * FROM proprietarios ")
        for linha in c.fetchall():
            placa = linha[0]
            nome = linha[1]
            matricula = linha[2]
            curso = linha[3]
            prop = Proprietario(nome, matricula, curso)
            self.cadastro_proprietarios[placa] = prop

    def armazenar_areas(self):
        c.execute("SELECT * FROM areas ")
        for linha in c.fetchall():
            nome = linha[0]
            capacidade = linha[1]
            categoria = linha[2]
            area = Areas(nome, capacidade, categoria)
            self.controle_areas.append(area)

    def armazenar_usuarios(self):
        c.execute("SELECT * FROM usuarios ")
        for linha in c.fetchall():
            nome = linha[0]
            cpf = linha[1]
            funcao = linha[2]
            setor = linha[3]
            usuario = linha[4]
            senha = linha[5]
            user = Usuario(nome, cpf, funcao, setor, usuario, senha)
            self.cadastro_usuario.append(user)

    def armazenar_ocorrencias(self):
        c.execute("SELECT * FROM ocorrencias ")
        for linha in c.fetchall():
            id = linha[0]
            tipo = linha[1]
            quantidade_veiculos = linha[2]
            data = linha[3]
            hora = linha[4]
            fatos = linha[5]
            ocorrencia = Ocorrencia(id, tipo, quantidade_veiculos, data, hora, fatos)
            self.cadastro_ocorrencias.append(ocorrencia)
            c.execute("SELECT * FROM veiculos_ocorrencias ")
            for linha in c.fetchall():
                id = linha[0]
                placa = linha[1]
                veiculo = self.validar_veiculo(placa.upper())
                ocorrencia.adicionar_veiculo(veiculo)




