n = int(input('Digite um número inteiro: '))
# Números primos precisam ser maiores do que 1
if n > 1:
  for i in range(2, n):
      if (n % i) == 0:
        print('Não é número primo!')
        break
  else:
      print('É um número primo!')
else:
    print('Não é um número primo!')