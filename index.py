# Аннуитетный платёж

total_summ = float(input('Введите сумму кредита: '))
total_years = int(input('На сколько лет выдан кредит? '))
percent = int(input('Сколько процентов годовых? '))

i = percent / 100
K = (i * (1 + i) ** total_years) / ((1 + i) ** total_years - 1)
A = round(K * total_summ, 2)

count = 1
for years in range(3):
    print('\nПериод:', count)
    count += 1
    print('\nОстаток долга на начало периода: ', total_summ)
    print('\nВыплачено процентов: ', total_summ * i)
    print('\nВыплачено тело кредита: ', A - total_summ * i)
    total_summ -= A - total_summ * i
print('\nОстаток долга ', total_summ)
print()
print('=======================')

extend = int(input('\nНа сколько лет продлевается договор? '))
new_percent = int(input('\nУвеличение ставки до: '))
total_years = total_years - count + 1 + extend

i = new_percent / 100
K = (i * (1 + i) ** total_years) / ((1 + i) ** total_years - 1)
A = round(K * total_summ, 2)

count = 1
for years in range(total_years):
    print('\nПериод:', count)
    count += 1
    print('\nОстаток долга на начало периода: ', total_summ)
    print('\nВыплачено процентов: ', total_summ * i)
    print('\nВыплачено тело кредита: ', A - total_summ * i)
    total_summ -= A - total_summ * i

print('\nОстаток долга ', total_summ)


#заработало?

#сумма ряда

import math


x = int(input('Введите x: '))
precision = float(input('Введите точность: '))
s = 1
degree = 2
s_temp = 1
count = 2
while s_temp > precision:
  if count % 2 == 0:
    s_temp = x ** degree / (math.factorial(degree))
    s -= s_temp
    count += 1
    degree += 2
  else:
    s_temp = x ** degree / (math.factorial(degree))
    s += s_temp
    count += 1
    degree += 2

print('Сумма ряда: ', s)