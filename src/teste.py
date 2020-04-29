from areas import Areas
from eventos import Eventos
from proprietario import Proprietario
from usuario import Usuario
from veiculo import Veiculo
from ocorrencias import Ocorrencia
from estacionamento import Estacionamento

estacionamento = Estacionamento()


#cadastrar area
estacionamento.cadastrar_area("Carros", 10, "carro")
estacionamento.cadastrar_area("Motos", 5, 'moto')
#cadastrar veiculo
estacionamento.cadastrar_veiculo('arthur', '20192007015', 'SI', 'aaa8830', 'gol', 'carro')
estacionamento.cadastrar_veiculo('iria', '20192007015', 'SI', 'bbb8830', 'gol', 'moto')
estacionamento.cadastrar_veiculo('joao', '20192007015', 'SI', 'ccc8830', 'gol', 'carro')
print('***veiculos cadastrados***')
for veiculo in estacionamento.get_cadastro_veiculos():
    print(veiculo)

#validar veiculo
print('***veiculo validado***')
print("validar veiculo = ", estacionamento.validar_veiculo('aaa8830'))

#remover veiculo
estacionamento.remover_veiculo('aaa8830')

print('**********************')
print('depois de remover veiculo:')
for veiculo in estacionamento.get_cadastro_veiculos():
    print(veiculo)

#cadastrar usuario
#user = Usuario('Arthur', '01233265748', 'gestor', 'Gerência', 'arthur', 'voltas28')
#estacionamento.cadastrar_usuario('Arthur', '01233265748', 'gestor', 'Gerência', 'arthur', 'voltas28')
#estacionamento.cadastrar_usuario('Ana', '01233265748', 'gestor', 'Gerência', 'aninha', '1515')
#for usuario in estacionamento.get_cadastro_usuario():
 #   print(usuario)

#print('***validacao****')

#print(estacionamento.login('arthur', 'voltas2'))

#cadastrar area

print('******************')
print('Areas:')

for area in estacionamento.get_controle_areas():
    print(area)

estacionamento.cadastrar_veiculo('arthur', '20192007015', 'SI', 'aaa8830', 'gol', 'carro')

estacionamento.validar_entrada('aaa8830')
estacionamento.validar_entrada('bbb8830')
estacionamento.validar_entrada('ccc8830')

print('**************')
print("mostrar areas: ")


for area in estacionamento.get_controle_areas():
    print(area.get_categoria())
    for veiculo in area.get_veiculos_area():
        print(veiculo)

print('******************')
print('Ocorrencias:')
estacionamento.cadastrar_ocorrencia(1, 'colisão', 2, '15/04/2020', '17:30', 'o veiculo xxx bateu na traseira do veiculo yyyy')

for ocorrencia in estacionamento.get_cadastro_ocorrencias():
    print(ocorrencia)

print('******************')
print('Eventos:')
estacionamento.cadastrar_evento('Inova', '25/05/2020', 5, 500)

for evento in estacionamento.get_controle_eventos():
    print(evento)
