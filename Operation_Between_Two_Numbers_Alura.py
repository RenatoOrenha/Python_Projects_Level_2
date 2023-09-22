# Operação entre dois números
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = input('Qual operação deseja realizar (+, -, x or /)? ')
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
if op == '+':
  print('O resultado é {}.'.format(s))
elif op == '-':
  print('O resultado é {}.'.format(sub))
elif op == 'x':
  print('O resultado é {}.'.format(mult))
elif op == '/':
  print('O resultado é {}.'.format(div))
else:
    print('Operador inválido!')
# Detalhes sobre o resultado:
# i) Par ou ímpar? ii) Positivo ou negativo? e iii) Inteiro ou decimal?
if s % 2 == 0:
  print('O resultado é par.')
else:
  print('O resultado é ímpar.')
if s > 0:
  print('O resultado é positivo.')
else:
  print('O resultado é negativo.')
if s % 1 == 0:
  print('O resultado é inteiro.')
else:
   print('O resultado é decimal.')