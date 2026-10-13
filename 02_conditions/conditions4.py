'''num = int(input())
summ = 0

while num > 0:                 #summa wseh cisel w stroke
    summ += num % 10
    num //= 10
print(summ)'''


'''num = int(input())
rev = 0
while num > 0:
    rev = rev * 10 + num % 10    #Задача Б2. Разворот числа.
    num //= 10
print(rev)'''

num = int(input())
while True:
    if num % 2 == 0:
        print(f'{}')