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
