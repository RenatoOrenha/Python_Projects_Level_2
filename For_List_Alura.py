# Lista com os números ordenados em ordem decrescente
lista = []

for i in range(0,5):
  n = int(input('Digite um número inteiro: '))
  lista.append(n)

new_element_0 = lista[4]
new_element_1 = lista[3]
new_element_2 = lista[2]
new_element_3 = lista[1]
new_element_4 = lista[0]
new_lista = [new_element_0, new_element_1, new_element_2, new_element_3, new_element_4]

print(new_lista)