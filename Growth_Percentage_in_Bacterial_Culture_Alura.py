# Dada a Lista do Número de Bactérias ao longo dos dias
lista = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# É calculado a porcentagem de crescimento da cultura ao longo dos dias
lista_p = []

for i in range(1, 9):
  p = 100 * (lista[i] - lista[i-1]) / (lista[i-1])
  lista_p.append('{:.0f}'.format(p))

print(lista_p)
