'''Задача 1
Пользователь вводит с экрана строчку Измените порядок символов в строке на обратный и распечатайте результат
Пример:
Ввод
Abdc
Вывод
cdbA'''

str1 = (input('Напиши что-то: '))
str2 = str1[::-1]
print(str2)

'''Задача 2
Вход записаны два числа, разделенные пробелом. Поменяйте их местами и напечатайте результат.
Пример:
Ввод
123 4
Вывод
4 123'''

input_numbers = input('Введи два числа через пробел: ')
numbers = input_numbers.split()
swapped_numbers = numbers[1] + " " + numbers[0]
print(swapped_numbers)

'''Задача 3
Программа считывает с клавиатуры число  n , и рисует звездочный квадрат размера  n∗n 
Пример:
Ввод
3
Вывод
***
***
***'''

n = int(input('Введи размер квадрата: '))
for i in range(n):
    row = "*" * n
    print(row)

'''Задача 4
Всё в том же детском саду ребята очень любят играть с цифрами. Одна из таких игр — перестановка цифр четырёхзначного числа. Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
Пример:
Ввод
1234
Вывод 2143'''

num4 = input('Введи четырехзначное число: ')
a, b, c, d = num4[0], num4[1], num4[2], num4[3]
new_num = b + a + d + c
print(new_num)

'''Задача 5
Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении. И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда. Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.
Пример:
Ввод
405
839
Вывод
234'''

x = input("Введите первое число: ")
y = input("Введите второе число: ")
result = ""
carry = 0
x = x[::-1]
y = y[::-1]
max_len = max(len(x), len(y))
x = f"{x:0{max_len}}"
y = f"{y:0{max_len}}"
for i in range(max_len):
    digit1 = int(x[i])
    digit2 = int(y[i])
    total = digit1 + digit2 + carry
    result += str(total % 10)
    carry = total // 10
if carry > 0:
    result += str(carry)
result = result[::-1]
print(result)

'''Задача 6
Иногда ребята в детском саду скучают, поэтому они постоянно придумывают себе не очень сложные, но веселые, по их мнению, игры. В группе есть ящик с шариками, количество которых детям заранее неизвестно, следующих цветов:
красный; зеленый; синий.
Игра заключается в том, что каждый ребенок подходит к ящику и, не глядя, вытаскивает один шарик, победителем считается тот, кто первым вытащит зелёный шарик. Как вы думаете, через какое максимальное количество ходов дети выяснят победителя игры?
Пример:
Ввод
1
2
3
Вывод
5'''

p = 1 / 3
max_moves = int(1 / (1 - p))
print(max_moves)


'''Задача 7
Продуктовый склад и магазин находятся на одной дороге города Н. Склад находится на отметке A км, а магазин — B км. Средняя скорость автомобиля, доставляющего товары, C км/ч. За какое время продукты попадают со склада в магазин?
Формат ввода Три натуральных числа A, B и C, каждое на отдельной строке.
Пример:
Ввод
10
32
5
Вывод
4.40'''

a = 32
b = 10
c = 5
time = (a-b)/c
print(time)









