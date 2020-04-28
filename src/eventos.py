class Eventos (object):
    def __init__(self, nome, data, vagas, zonas):
        self.nome = nome
        self.data = data
        self.vagas = vagas
        self.zonas = zonas

    #Getters & Setters

    def nome(self):
        return self.nome

    def nome (self, nome):
        self._nome = nome


    def data(self):
        return self.data

    def data(self, data):
        self._data = data


    def vagas(self):
        return self.vagas

    def vagas(self, vagas):
        self.vagas = vagas


    def zonas(self):
        return self.zonas

    def zonas(self, zonas):
        self.__zonas = zonas

    #To String
    def __str__(self):
        return ("Nome: {} "
        "\nData: {}"
        "\nVagas: {}"
        "\nZonas: {}".format(self.nome, self.data, self.vagas, self.zonas))

a = Eventos("Inova", "25/11/2020", 1500, "A,B,C")
print(a)

