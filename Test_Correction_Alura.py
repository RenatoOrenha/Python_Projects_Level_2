count_Q1 = 0
count_Q2 = 0
count_Q3 = 0
count_Q4 = 0
count_Q5 = 0
count_Q6 = 0
count_Q7 = 0
count_Q8 = 0
count_Q9 = 0
count_Q10 = 0

Gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

for i in range(0, 10):
    i = input('Digite a alternativa correta (A, B, C ou D): ')
    if i == Gabarito[0]:
        count_Q1 += 1
    elif i == Gabarito[1]:
        count_Q2 += 1
    elif i == Gabarito[2]:
        count_Q3 += 1
    elif i == Gabarito[3]:
        count_Q4 += 1
    elif i == Gabarito[4]:
        count_Q5 += 1
    elif i == Gabarito[5]:
        count_Q6 += 1
    elif i == Gabarito[6]:
        count_Q7 += 1
    elif i == Gabarito[7]:
        count_Q8 += 1
    elif i == Gabarito[8]:
        count_Q9 += 1
    elif i == Gabarito[9]:
        count_Q10 += 1

soma = count_Q1 + count_Q2 + count_Q3 + count_Q4 + count_Q5 + count_Q6 + count_Q7 + count_Q8 + count_Q9 + count_Q10

print(soma)
