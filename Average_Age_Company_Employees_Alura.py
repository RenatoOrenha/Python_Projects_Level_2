# Idade média por setor e geral em uma empresa
idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

count_idade_sup = 0

media_idade_setor_lista = []

for setor, idade in idades.items():
  media_idade_setor = sum(idade) / 10
  media_idade_setor_lista.append(media_idade_setor)
  print('A média de idade no {} é igual a {:.0f}'.format(setor, media_idade_setor))

media_global = (media_idade_setor_lista[0] + media_idade_setor_lista[1] + media_idade_setor_lista[2] + media_idade_setor_lista[3])  / 4

# Número de pessoas com idade superior ao da média geral da empresa
for setor, idade in idades.items():
  for id in idade:
    if id > media_global:
      count_idade_sup += 1

print('A média geral entre todos os setores é igual a {:.0f}'.format(media_global))
print('O número de pessoas com idade acima da média geral é igual a {:.0f}.'.format(count_idade_sup))

