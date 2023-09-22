# Cálculo do preço do combustivel E (Etanol) ou D (Diesel)
# Feito a partir da quantidade de litros solicitada para o abastecimento
frase1 = input('Qual o combustível: E ou D? ')
frase2 = float(input('Qual a quantidade em litros? '))

# Desconto de 2 e 3 % para E e D, respectivamente
# para abastecimento menor ou igual a 15 L
# Desconto de 4 e 5 % para E e D, respectivamente
# para abastecimento maior do que 15 L

preco1_E = 1.7 * frase2 * 0.98
preco2_E = 1.7 * frase2 * 0.96
preco1_D = 2 * frase2 * 0.97
preco2_D = 2 * frase2 * 0.95

if frase1 == 'E' and frase2 <= 15:
  print('O valor a ser pago pelo cliente é {}.'.format(preco1_E))
elif frase1 == 'E' and frase2 > 15:
  print('O valor a ser pago pelo cliente é {}.'.format(preco1_E))
if frase1 == 'D' and frase2 <= 15:
  print('O valor a ser pago pelo cliente é {}.'.format(preco1_D))
elif frase1 == 'D' and frase2 > 15:
  print('O valor a ser pago pelo cliente é R$ {}.'.format(preco2_D))

