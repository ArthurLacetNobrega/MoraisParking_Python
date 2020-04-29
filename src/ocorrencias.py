class Ocorrencia():
    """Representa as ocorrencias, relacionadas a danos,  que acontecem dentro do estacionamento"""

    def __init__(self, id, tipo, quantidade_veiculos, data, hora, fatos):
        self.id = id
        self.tipo = tipo
        self.quantidade_veiculos = quantidade_veiculos
        self.veiculos_ocorrencias = list()
        self.data = data
        self.hora = hora
        self.fatos = fatos

    #Getter & Setter
    def get_id(self):
        return self.id

    def set_id(self):
        self.id = id

    def get_tipo(self):
        return self.tipo

    def set_tipo (self, tipo):
        self.tipo = tipo

    def get_quantidade_veiculos(self):
        return self.quantidade_veiculos

    def set_quantidade_veiculos(self, quantidade_veiculos):
        self.quantidade_veiculos = quantidade_veiculos

    def get_veiculos_ocorrencias(self):
        return self.veiculos_ocorrencias

    def set_veiculos_ocorrencias(self, veiculos_ocorrencias):
        self.veiculos_ocorrencias = veiculos_ocorrencias

    def get_data(self):
        return self.data

    def get_data(self, data):
        self.data = data

    def get_hora(self):
        return self._hora

    def set_hora(self, hora):
        self.hora = hora

    def get_fatos(self):
        return self.fatos

    def set_fatos(self, fatos):
        self.fatos = fatos

    # Methods
    def adicionar_veiculo(self, veiculo):
        self.veiculos_ocorrencias.append(veiculo)

    #To String
    def __str__(self):
        return "ID: %s\n Tipo: %s\n Quantidade de Veículos: %d\n Veículos: %s\n Data: %s\n Hora: %s\n Fatos: %s\n" %(self.id, self.tipo, self.quantidade_veiculos, self.veiculos_ocorrencias, self.data, self.hora, self.fatos)



