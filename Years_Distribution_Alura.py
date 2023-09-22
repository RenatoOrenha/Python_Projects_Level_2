# Distribuição de Idades nas faixas:
# 0-25; 26-50; 51-75 e 76-100
n = int(input('Digite a sua idade (valor negativo encerra o processo): '))

contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

while n >= 0:
    if n > 0 and n <= 25:
        contador_0_25 += 1
    elif n > 25 and n <= 50:
        contador_26_50 += 1
    elif n > 50 and n <= 75:
        contador_51_75 += 1
    elif n > 75 and n <= 100:
        contador_76_100 += 1

# A idade será perguntada até que um valor negativo seja digitado
    n = int(input('Digite a sua idade (valor negativo encerra o processo): '))

print('Resultado da Distribuição de Idades')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)