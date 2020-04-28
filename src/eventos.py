class Eventos ():
    def __init__(self, nome, data, vagas, zonas):
        self.nome = nome
        self.data = data
        self.vagas = vagas
        self.zonas = zonas

    #Getters & Setters

    def get_nome(self):
        return self.nome

    def set_nome (self, nome):
        self._nome = nome


    def get_data(self):
        return self.data

    def set_data(self, data):
        self._data = data


    def get_vagas(self):
        return self.vagas

    def set_vagas(self, vagas):
        self.vagas = vagas


    def get_zonas(self):
        return self.zonas

    def set_zonas(self, zonas):
        self.__zonas = zonas

    #To String
    def __str__(self):
        return ("Nome: {} "
        "\nData: {}"
        "\nVagas: {}"
        "\nZonas: {}".format(self.nome, self.data, self.vagas, self.zonas))



