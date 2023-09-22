# Análise de Diversidade Biológica nas áreas Norte, Leste, Sul, Oeste e Centro
# Valores presentes nas listas são referentes as espécies de plantas e animais, respectivamente
dic = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

soma_especies_lista = []

# Média das espécies (plantas + animais)/2 por área
for area, especies in dic.items():
  media_especies = sum(especies) / 2
  print('A média das espécies na {} é igual a {:.0f}.'.format(area, media_especies))
  soma_especies = sum(especies)
  soma_especies_lista.append(soma_especies)

# Avaliação da área com maior diviersidade de espécies ou soma das populações de espécies
if soma_especies_lista[0] >  soma_especies_lista[1] and soma_especies_lista[0] >  soma_especies_lista[2] and soma_especies_lista[0] >  soma_especies_lista[3] and soma_especies_lista[0] >  soma_especies_lista[4]:
  print('Área Norte tem a maior diversidade biológica!')
elif soma_especies_lista[1] >  soma_especies_lista[0] and soma_especies_lista[1] >  soma_especies_lista[2] and soma_especies_lista[1] >  soma_especies_lista[3] and soma_especies_lista[1] >  soma_especies_lista[4]:
  print('Área Leste tem a maior diversidade biológica!')
elif soma_especies_lista[2] >  soma_especies_lista[0] and soma_especies_lista[2] >  soma_especies_lista[1] and soma_especies_lista[2] >  soma_especies_lista[3] and soma_especies_lista[2] >  soma_especies_lista[4]:
  print('Área Sul tem a maior diversidade biológica!')
elif soma_especies_lista[3] >  soma_especies_lista[0] and soma_especies_lista[3] >  soma_especies_lista[1] and soma_especies_lista[3] >  soma_especies_lista[2] and soma_especies_lista[3] >  soma_especies_lista[4]:
  print('Área Oeste tem a maior diversidade biológica!')
else:
  print('Área Centro tem a maior diversidade biológica!')
