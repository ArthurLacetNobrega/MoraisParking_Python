class Ocorrencia():

    def __init__(self, categoria, quantidade_veiculos, data, hora, fatos):
        self.categoria = categoria
        self.quantidade_veiculos = quantidade_veiculos
        self.veiculos_ocorrencias = list()
        self.data = data
        self.hora = hora
        self.fatos = fatos

    #Getter & Setter
    def get_categoria(self):
        return self.categoria

    def set_categoria (self, categoria):
        self.categoria = categoria


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

