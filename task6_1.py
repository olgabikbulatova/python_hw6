# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

lst = [random.randint(1, 25) for i in range(15)]
min_a = int(input('введите минимальное значение: '))
max_a = int(input('введите максимальное значение: '))
print(*lst)
lst_2 = []
for i in range (len(lst)):
    if min_a < lst[i] < max_a:
        lst_2.append(i)
print(*lst_2)
