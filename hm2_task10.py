# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

from random import randint
n=int(input("Введите количество монеток: "))
count_0=0
count_1=0
for i in range(n):
    s=randint(0,1)
    print(s)
    if s==0:
        count_0+=1
    else: count_1+=1
if count_0>count_1:
    print(f'перевернуть нужно {count_1}')
else:
    print(f'перевернуть нужно {count_0}')