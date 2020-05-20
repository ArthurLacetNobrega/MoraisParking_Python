import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

class Eventos():
    """Representa os eventos que podem acontecer, que reduzem a capacidade e modificam o acesso de veiculos"""

    def __init__(self, nome, data_inicio, duracao, vagas):
        self.nome = nome
        self.data_inicio = data_inicio
        self.duracao = duracao
        self.vagas = vagas


    #To String
    def __str__(self):
        return f'Nome: {self.nome}\nData de Realização: {self.data_inicio}\nDuração: {self.duracao} Vagas: {self.vagas}'

    def __repr__(self):
        return f'Nome: {self.nome} Data de Realização: {self.data_inicio} Duração: {self.duracao}'

    #criar tabela
    #método estático para criação do método
    @staticmethod
    def criar_tabela():
        try:
            c.execute(
                'CREATE TABLE IF NOT EXISTS eventos (nome text, data_inicio text, duracao text, vaga text)')
        except:
            print('Erro ao criar a tabela')

    '''Metodo usada para buscar todos os itens da tabela eventos'''
    @staticmethod
    def all():
        try:
            r = c.execute('SELECT * FROM eventos')
        except:
            print('Erro ao fazer consulta')
        else:
            return r.fetchall()


    def salvar(self):
        '''cadastrando evento, a função sera chamada em estacionamento.py '''
        print("CADASTRO DE EVENTOS")
        try:
            c.execute("INSERT INTO eventos VALUES (?, ?, ?, ?)",
                      (self.nome, self.data_inicio, self.duracao, self.vagas))
            con.commit()
        except:
            print("HOUVE UM ERRO!")
        else:
            print("ADICIONADO!")

    @staticmethod
    def cadastrar_evento():
        print('************ CADASTRAR EVENTO *************')
        Eventos(input("Nome: "), input("Data de Inicio: "), input("Duracao: "), input("Vagas")).salvar()

    @staticmethod
    def consultar_evento_por_nome():
        evento = Eventos.buscar_por_nome()
        if evento:
            print(f'Evento: {evento}')
        else:
            print("Evento não encontrado")

    @staticmethod
    def buscar_por_nome():
        return Eventos.buscar_evento(input("Digite o nome do Evento: "))

    @staticmethod
    def buscar_evento(nome):
        try:
            r = c.execute('SELECT * FROM eventos WHERE nome = ?', (nome,))
            evento = r.fetchone()
            print(evento)
        except:
            print('Erro ao fazer consulta')
            evento = None
        finally:
            return evento

    @staticmethod
    def consultar_eventos():
        for evento in Eventos.all():
            print(f'Evento: {evento}')

    @staticmethod
    def remover_evento():
        Eventos.excluir_evento(input("Nome do evento:"))

    @staticmethod
    def excluir_evento(nome):
        try:
            c.execute('DELETE FROM eventos WHERE nome = ?', (nome,))
            con.commit()
            print(f"O evento {nome} foi excluido com sucesso")
        except:
            print('Erro ao fazer EXCLUSÃO')

    @staticmethod
    def atualizar_evento():
        Eventos.atualizar_evento_por_nome(input("Nome do evento:"))

    @staticmethod
    def ler_campo(valor_atual, campo):
        valor_lido = input(f'{campo}')
        return valor_atual if valor_lido == '' else valor_lido

    @staticmethod
    def atualizar_evento_por_nome(nome):
        evento = Eventos.buscar_evento(nome)
        if evento:
            nome_atual, data_inicio_atual, duracao_atual, vagas_atual = evento
            nome = Eventos.ler_campo(nome_atual, "Novo Nome: ")
            data_inicio = Eventos.ler_campo(data_inicio_atual, "Nova data: ")
            duracao = Eventos.ler_campo(duracao_atual, "Nova Duração: ")
            vagas = Eventos.ler_campo(vagas_atual, "Novo número de vagas: ")
            try:
                c.execute("""UPDATE eventos SET 
                        nome = ?, data_inicio = ?, duracao = ?, vaga = ? WHERE nome = ?""",
                          (nome, data_inicio, duracao, vagas, nome_atual))
                con.commit()
                print(f"O evento {nome} foi atualizado com sucesso")
            except:
                print('Erro ao fazer ATUALIZAÇÃO')