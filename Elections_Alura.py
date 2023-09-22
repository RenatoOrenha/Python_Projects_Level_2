# Número inicial de votos de cada candidato, nulos e brancos
cont_candidato_1 = 0
cont_candidato_2 = 0
cont_candidato_3 = 0
cont_candidato_4 = 0
cont_nulos = 0
cont_brancos = 0

# A eleição terá 20 eleitores
for i in range(0,20):
  voto = int(input('Informe seu voto: '))
  if voto == 1:
    cont_candidato_1 += 1
  elif voto == 2:
    cont_candidato_2 += 1
  elif voto == 3:
    cont_candidato_3 += 1
  elif voto == 4:
    cont_candidato_4 += 1
  elif voto == 5:
    cont_nulos += 1
  elif voto == 6:
    cont_brancos += 1
  else:
    print('Voto Inválido')

nulos = (cont_nulos * 100) / (cont_candidato_1 + cont_candidato_2 + cont_candidato_3 + cont_candidato_4 + cont_nulos + cont_brancos)
brancos = (cont_brancos * 100) / (cont_candidato_1 + cont_candidato_2 + cont_candidato_3 + cont_candidato_4 + cont_nulos + cont_brancos)

print('Resultado das Eleições:')
print('Nº de Votos do Candidato 1:', cont_candidato_1)
print('Nº de Votos do Candidato 2:', cont_candidato_2)
print('Nº de Votos do Candidato 3:', cont_candidato_3)
print('Nº de Votos do Candidato 4:', cont_candidato_4)
print('Nº de Votos Nulos:', cont_nulos)
print('Nº de Votos Brancos:', cont_brancos)
print('Porcentagem de Votos Nulos: {:.0f}'.format(nulos))
print('Porcentagem de Votos Brancos: {:.0f}'.format(brancos))
