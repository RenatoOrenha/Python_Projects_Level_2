lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
count_m_3000 = 0

for elemento in lista[:]:
  if elemento > 3000:
    count_m_3000 += 1

print(count_m_3000)
p = (100 * count_m_3000) / len(lista)
print('{:.0f} %'.format(p))