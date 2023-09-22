# Contabilidade de Empresa
lista = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

abono = {}

count_200 = 0

for i in lista:
  increase = 0.1 * i
  if increase < 200:
    abono[i] = 200
    count_200 += 1
  else:
    abono[i] = increase

tg = (abono[1172] + abono[1644] + abono[2617] + abono[5130] + abono[5532] + abono[6341] + abono[6650] + abono[7238] + abono[7685] + abono[7782] + abono[7903])

max_value = max(abono.values())

# i) Cálculo do abono de salário de cada funcionário; ii) total de gastos com abono; iii) número de colaboradores que receberam o abono mínimo; e
# iv) maior abono fornecido.

print('Abono: {}'.format(abono))
print('O total de gastos com abono é {:.0f}'.format(tg))
print('O número de colaboradoes que receberam o abono mínimo é {:.0f}.'.format(count_200))
print('O maior valor de abono fornecido foi de {:.0f}.'.format(max_value))
