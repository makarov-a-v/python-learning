

'''for i in range(5): # 5 раз с нуля
    print(i, "Привет")

for i in range(3):   #C нуля
    text = input()
    print(i, text)

for i in range(1, 5): # от 1 до 4
    text = input()
    print(i, text)'''
from itertools import count

'''for i in range(1, 11, 2):  #от 1 до 10 через 2
    text = "Text" #input()
    print(i, text)'''

'''count = 0
while count <= 5:
    print("Hi")
    count += 1'''

'''result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break   #учитывает число с отрицательным числом и останавливается когда его вводишь
    result += num

print("Сумма введнных всех чисел: ", result)'''

'''result = 0
for i in range(4):
    num = int(input())
    if num < 0:
        continue #учитывает число с отрицательным числом но не считает его и игнорирует. 
    result += num

print("Сумма введнных всех чисел: ", result)'''

'''for i in range(1, 31):
    if i == 7 or i == 17 or i == 29:
        continue  # переходим на следующую итерацию (и не доходим до print)
    print(i)'''

'''
while n > 0:
    for i in range(1, 31):
        if n % i == 0:
            break'''

'''for i in range(3, 10, 3):
    print(i)'''


'''n = int(input())
summ = 0
for i in range(1, n+1):
    summ += i

print(summ)'''

'''n = int(input())
summ = 0
for i in range(1, n+1):
    if summ % 2 == 0:
        summ += i
print(summ)'''

#Задание 1. Выведи в терминал числа 3, 6, 9, используя цикл for и функцию range.
'''for i in range (3, 10, 3):
    print(i)'''

#Задание 2. Дано число n (вводится с клавиатуры). Посчитай сумму чисел от 1 до n включительно, выведи результат.
'''n = int(input())
summ = 0

for i in range(1, n+2):
    summ += i
print(summ)'''


'''n = int(input())
summ = 0

for i in range(1, n+1):
    if i % 2 == 0:
        summ += i
print(summ)'''



'''summ = 0
for i in range(10):
    n = int(input())
    if n < 0:
        break
    summ += n
print(summ)'''

'''for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)'''

'''summ = 0
count = 0
while True:
    n = int(input())  # SREDNEE ARIFM
    if n == 0:
        break
    summ += n
    count += 1
if count > 0:
    print(summ / count)
else:
    print('Где числа?')'''



'''n = int(input())
maximum = n
minimum = n

for i in range(9):
    n = int(input())  # NAH min max
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print(maximum)
print(minimum)'''


'''
x = 7
y = 1

while y <= 10:
    print(f"{x} * {y} = {x * y}")   # таблица умн (for i in range(1, 11))(выбирают, когда количество итераций известно, а while — когда есть условие остановки.выбирают, когда количество итераций известно, а while — когда есть условие остановки.
    y += 1
'''

'''
n = int(input())
for i in range(1, n + 1): # «использовать счётчик цикла как число повторений»
    print("*" * i)'''


'''# Прямоуголник( вложенные циклы)
weight = int(input())
height = int(input())

for i in range(height):
    for j in range(weight):
        print("#", end="")

    print()'''

'''#последняя, со звёздочкой). FizzBuzz

for i in range(1, 50 + 1):
    if i % 3 ==0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)'''
