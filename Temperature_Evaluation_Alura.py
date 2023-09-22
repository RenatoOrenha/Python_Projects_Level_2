# Construir Lista de Temperaturas do Mês ao longo do Ano
lista = []

lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(0,12):
  temperatura = float(input('Digite a temperatura média do mês: '))
  lista.append(temperatura)

media = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + lista[5] + lista[6] + lista[7] + lista[8] + lista[9] + lista[10] + lista[11]) / 12

print(media)

# Avaliar quais meses obtiveram temperaturas acima da média de temperatura anual
for i in range(0, 12):
  if lista[i] > media:
    print('{}: {}'.format(lista_mes[i], lista[i]))




