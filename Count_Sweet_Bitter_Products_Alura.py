# Contagem do Número de Produtos Doces e Amargos
# Produto doce contém ID par
# Produto amargo contém ID ímpar
cont_ID_par = 0
cont_ID_impar = 0

for i in range(0, 10):
  ID = int(input('Digite o número do ID do produto: '))
  if ID % 2 == 0:
    cont_ID_par += 1
  else:
    cont_ID_impar +=1

print('O número de produtos doces é {:.0f}'.format(cont_ID_par))
print('O número de produtos amargos é {:.0f}'.format(cont_ID_impar))

