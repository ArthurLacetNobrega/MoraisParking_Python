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


    #Getters & Setters
    def get_nome(self):
        return self.nome

    def set_nome (self, nome):
        self._nome = nome

    def get_data_inicio(self):
        return self.data_inicio

    def set_data_inicio(self, data_inicio):
        return self.data_inicio

    def get_duracao(self):
        return self.duracao

    def set_duracao(self, duracao):
        self.duracao = duracao

    def get_vagas(self):
        return self.vagas

    def set_vagas(self, vagas):
        self.vagas = vagas

    #To String
    def __str__(self):
        return "Nome: %s\nData de Realização: %s\nDuração: %d\nVagas: %d" % (self.nome, self.data_inicio, self.duracao, self.vagas)


    def cadastro_evento(self, nome, data_inicio, duracao, vagas):
        '''cadastrando evento, a função sera chamada em estacionamento.py '''
        evento = Eventos(nome.upper(), data_inicio.upper(), duracao.upper(), vagas.upper())
        c.execute(
            'CREATE TABLE IF NOT EXISTS cadastro_de_eventos(nome TEXT PRIMARY KEY, data_inicio TEXT, duracao TEXT, vagas TEXT)')
        c.execute('INSERT INTO evento VALUES (?, ?, ?, ?)',
                  (evento.get_nome(), evento.get_data_inicio(), evento.get_duracao(), evento.get_vagas()))
        con.commit()
        self.armazenar_eventos()


    def armazenar_eventos(self):
        c.execute("SELECT * FROM proprietarios ")
        for linha in c.fetchall():
            nome = linha[0]
            data_inicio = linha[1]
            duracao = linha[2]
            vaga = linha[3]
            eve = Eventos(nome, data_inicio, duracao, vaga)
