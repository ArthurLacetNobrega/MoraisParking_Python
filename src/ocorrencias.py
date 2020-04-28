class Ocorrencia(object):

    def __init__(self, categoria, quantidade_veiculos, data, hora, fatos):
        self.categoria = categoria
        self.quantidade_veiculos = quantidade_veiculos
        self.veiculos_ocorrencias = list()
        self.data = data
        self.hora = hora
        self.fatos = fatos

    #Getter & Setter
    def categoria(self):
        return self.categoria

    def categoria (self, categoria):
        self.categoria = categoria


    def quantidade_veiculos(self):
        return self.quantidade_veiculos

    def quantidade_veiculos(self, quantidade_veiculos):
        self.quantidade_veiculos = quantidade_veiculos


    def veiculos_ocorrencias(self):
        return self.veiculos_ocorrencias


    def veiculos_ocorrencias(self, veiculos_ocorrencias):
        self.veiculos_ocorrencias = veiculos_ocorrencias


    def data(self):
        return self.data

    def data(self, data):
        self.data = data


    def hora(self):
        return self._hora


    def hora(self, hora):
        self.hora = hora


    def fatos(self):
        return self.fatos


    def fatos(self, fatos):
        self.fatos = fatos

    #To String
    def __str__(self):
        return ("Categoria: {} "
        "\nQuantidade de Veículos: {}"
        "\nData: {}"
        "\nHora: {}"
        "\nFatos: {}".format(self.categoria, self.quantidade_veiculos, self.data, self.hora, self.fatos))

    #Methods
    def cadastrar_veiculo_ocorrencias(self, veiculo):
        self.veiculos_ocorrencias().append(veiculo)

