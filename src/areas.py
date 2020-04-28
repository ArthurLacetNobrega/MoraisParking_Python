class Areas():
    def __init__(self, nome, capacidade, categoria):
        self.nome = nome
        self.capacidade = capacidade
        self.categoria = categoria
        self.veiculos_area = list()

    #Getter & Setter
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_veiculos_area(self):
        return self.veiculos_area

    #Methods
    def entrada_veiculo(self, veiculo):
        self.veiculos_area.append(veiculo)

    def saida_veiculo(self, veiculo):
        self.veiculos_area.remove(veiculo)

    def mostrar_area(self):
        for veiculo in self.veiculos_area():
            print(veiculo)

     #To String
    def __str__(self):
        return (" Nome: {} "
        "\n Categoria: {}"
        "\n Capacidade: {}".format(self.nome,self.categoria,self.capacidade))







