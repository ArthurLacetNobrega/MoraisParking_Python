from areas import Areas
from eventos import Eventos
from proprietario import Proprietario
from usuario import Usuario
from veiculo import Veiculo
from ocorrencias import Ocorrencia
from estacionamento import Estacionamento

estacionamento = Estacionamento()

#cadastrar categoria
#categ = estacionamento.adicionar_categoria('carro')

#print(estacionamento.get_categorias())

#estacionamento.validar_cetegoria('moto')

#cadastrar veiculo
#nome = input("Insira o nome do Proprietário: ").upper()
#matricula = input("Insira a matricula, caso aplicável: ").upper()
#curso = input("Insira o curso, caso aplicável: ").upper()
#placa = input("Insira a placa do veículo: ").upper()
#modelo = input("Insira o modelo do veículo: ").upper()
#categoria = estacionamento.validar_cetegoria(input("Insira a categoria: "))
estacionamento.cadastrar_veiculo('arthur', '20192007015', 'SI', 'OFH8830', 'gol', 'carro')
estacionamento.cadastrar_veiculo('iria', '20192007015', 'SI', 'OFX8830', 'gol', 'moto')

#for veiculo in estacionamento.get_cadastro_veiculos():
 #  print(veiculo)

#validar veiculo

#print(estacionamento.validar_veiculo('ofh8830'))

#remover veiculo
#estacionamento.remover_veiculo('ofh8830')

#for veiculo in estacionamento.get_cadastro_veiculos():
 #  print(veiculo)

#cadastrar usuario
#user = Usuario('Arthur', '01233265748', 'gestor', 'Gerência', 'arthur', 'voltas28')
#estacionamento.cadastrar_usuario('Arthur', '01233265748', 'gestor', 'Gerência', 'arthur', 'voltas28')
#estacionamento.cadastrar_usuario('Ana', '01233265748', 'gestor', 'Gerência', 'aninha', '1515')
#for usuario in estacionamento.get_cadastro_usuario():
 #   print(usuario)

#print('***validacao****')

#print(estacionamento.login('arthur', 'voltas2'))

#cadastrar area

estacionamento.cadastrar_area("Carros", 10, "carro")
estacionamento.cadastrar_area("Motos", 5, "moto")

#for area in estacionamento.get_controle_areas():
#    print(area)

estacionamento.validar_entrada('ofh8830')
estacionamento.validar_entrada('OFX8830')

for area in estacionamento.get_controle_areas():
    print(area.mostrar_area())
