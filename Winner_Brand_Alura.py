# Dicionário contendo uma tabela de votos de diferentes marcas
TVM = {
'Design 1': 1334,
'Design 2':  982,
'Design 3': 1751,
'Design 4':  210,
'Design 5': 1811
}

# Porcentagem de votos obtidos em cada uma das marcas
p0 = (100 * TVM['Design 1']) / (TVM['Design 1'] + TVM['Design 2'] + TVM['Design 3'] + TVM['Design 4'] + TVM['Design 5'])
p1 = (100 * TVM['Design 2']) / (TVM['Design 1'] + TVM['Design 2'] + TVM['Design 3'] + TVM['Design 4'] + TVM['Design 5'])
p2 = (100 * TVM['Design 3']) / (TVM['Design 1'] + TVM['Design 2'] + TVM['Design 3'] + TVM['Design 4'] + TVM['Design 5'])
p3 = (100 * TVM['Design 4']) / (TVM['Design 1'] + TVM['Design 2'] + TVM['Design 3'] + TVM['Design 4'] + TVM['Design 5'])
p4 = (100 * TVM['Design 5']) / (TVM['Design 1'] + TVM['Design 2'] + TVM['Design 3'] + TVM['Design 4'] + TVM['Design 5'])

# Indicar a marca mais votada
if TVM['Design 1'] > TVM['Design 2'] and TVM['Design 1'] > TVM['Design 3'] and TVM['Design 1'] > TVM['Design 4'] and TVM['Design 1'] > TVM['Design 5']:
  print('Design 1 foi a marca mais votada!')
  print('A porcentagem de votos recebidos é {:.0f}'.format(p0))
elif TVM['Design 2'] > TVM['Design 1'] and TVM['Design 2'] > TVM['Design 3'] and TVM['Design 2'] > TVM['Design 4'] and TVM['Design 2'] > TVM['Design 5']:
  print('Design 2 foi a marca mais votada!')
  print('A porcentagem de votos recebidos é {:.0f}'.format(p1))
elif TVM['Design 3'] > TVM['Design 1'] and TVM['Design 3'] > TVM['Design 2'] and TVM['Design 3'] > TVM['Design 4'] and TVM['Design 3'] > TVM['Design 5']:
  print('Design 3 foi a marca mais votada!')
  print('A porcentagem de votos recebidos é {:.0f}'.format(p2))
elif TVM['Design 4'] > TVM['Design 1'] and TVM['Design 4'] > TVM['Design 2'] and TVM['Design 4'] > TVM['Design 2'] and TVM['Design 4'] > TVM['Design 5']:
  print('Design 4 foi a marca mais votada!')
  print('A porcentagem de votos recebidos é {:.0f}'.format(p3))
else:
  print('Design 5 foi a marca mais votada!')
  print('A porcentagem de votos recebidos é {:.0f} %'.format(p4))


