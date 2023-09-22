# Avaliação do aumento ou diminuição da porcentagem de vendas
# O resultado define a estratégia da empresa
Qtde_Vendas_2022 = float(input('Digite a quantidade de venda durante os ano de 2022: '))
Qtde_Vendas_2023 = float(input('Digite a quantidade de venda durante os ano de 2023: '))
VP = ((Qtde_Vendas_2023 - Qtde_Vendas_2022) / Qtde_Vendas_2022) * 100
if VP > 20:
  print('Bonificação para o time de vendas!')
elif 2 < VP and VP < 20:
  print('Pequena bonificação para time de vendas.')
elif -10 < VP and VP < 2:
  print('Planejamento de políticas de incentivo às vendas.')
else:
  print('Corte de gastos ...')