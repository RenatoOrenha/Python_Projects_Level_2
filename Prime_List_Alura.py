lista = []

n = int(input('Digite um número inteiro: '))

for i in range(2, n):
  primo = True
  for j in range(2, i):
      if (i % j) == 0:
        primo = False
        break
  if primo:
    lista.append(i)

print(lista)