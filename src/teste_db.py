from estacionamento import *
from areas import Areas
from datetime import datetime


estacionamento = Estacionamento()

estacionamento.validar_entrada('aaa1234')

for veiculo in areas.get_veiculos_area():
    print(veiculo)