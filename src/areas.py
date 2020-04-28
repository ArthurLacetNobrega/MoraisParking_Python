class Areas(object):
    def __init__(self, nome, capacidade, categoria):
        self.nome = nome
        self.capacidade = capacidade
        self.categoria = categoria
        self.veiculos_area = list()

    #Getter & Setter
    def nome(self):
        return self.nome

    def nome(self, nome):
        self.nome = nome


    def capacidade(self):
        return self.capacidade

    def capacidade(self, capacidade):
        self.capacidade = capacidade


    def categoria(self):
        return self.categoria

    def categoria(self, categoria):
        self.categoria = categoria


    def veiculos_area(self):
        return self.veiculos_area

    def veiculos_area (self,veiculos_area):
        self.veiculos_area = veiculos_area

    #To String
    def __str__(self):
        return (" Nome: {} "
        "\n Categoria: {}"
        "\n Capacidade: {}".format(self.nome,self.categoria,self.capacidade))

    #Methods

    def entrada_veiculo(self, veiculo):
        self.veiculos_area.append(veiculo)

    def saida_veiculo(self, veiculo):
        self.veiculos_area.remove(veiculo)

p = Areas("B", 200, "Carro")
print(p)





