Vendas_Produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

soma = (Vendas_Produtos['Produto A'] + Vendas_Produtos['Produto B'] + Vendas_Produtos['Produto C'] + Vendas_Produtos['Produto D'] + Vendas_Produtos['Produto E'] + Vendas_Produtos['Produto F'])

print('O total de vendas é {:.0f}'.format(soma))

if Vendas_Produtos['Produto A'] > Vendas_Produtos['Produto B'] and Vendas_Produtos['Produto A'] > Vendas_Produtos['Produto C'] and Vendas_Produtos['Produto A'] > Vendas_Produtos['Produto D']:
  print('Produto A é o mais vendido!')
elif Vendas_Produtos['Produto B'] > Vendas_Produtos['Produto A'] and Vendas_Produtos['Produto B'] > Vendas_Produtos['Produto C'] and Vendas_Produtos['Produto B'] > Vendas_Produtos['Produto D']:
  print('Produto B é o mais vendido!')
elif Vendas_Produtos['Produto C'] > Vendas_Produtos['Produto A'] and Vendas_Produtos['Produto C'] > Vendas_Produtos['Produto B'] and Vendas_Produtos['Produto C'] > Vendas_Produtos['Produto D']:
  print('Produto C é o mais vendido!')
else:
    print('Produto D é o mais vendido!')


