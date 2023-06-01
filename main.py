# import math
# a = int(input("введите длину первого катета:"))
# b = int(input("введите длину второго катета:"))
# # c гипотенуза
# #a**2+b**2=c**2
# c = math.sqrt(a**2+b**2)
# print(c)
# d= math.hypot(3,8)
# print(d)

import random
a = random.randint(-1000,1000)
b = random.randint(-1000,1000)
print(a,b)
if a%2 == 0 and b%2 ==1:
    print(b, "нечетное")
elif b%2 == 0 and a%2 == 1:
    print(a, "нечетное")
elif b%2 == 0 and a%2 == 0:
    print(a,b, "четные оба числа")
elif a%2 == 0 and b == 0 or b%2 == 0 and a == 0:
    print("нет нечетных чисел")


print("########################################################")


# a = str(int(input("Введите число:")))
# a_inverse = a[::-1]
# print(a_inverse)

# a = int(input("Введите число 1, если фигура прямоугольник, 2 - если треугольник и 3 - если круг"))
# if a == 1:
#     m = int(input("Введите сторону фигуры в мм"))
#     k = int(input("Введите сторону фигуры в мм"))
#     print(m*k)
# elif b == 2:
#
#     print()
# elif c == 3:
#     print():
# else:
#     print("Вы неправильно ввели номер фигуры")


# a = int(input("введите длину первой стороны :"))
# b = int(input("введите длину второй стороны :"))
# c = int(input("введите длину третьей стороны :"))
# if a+b>c and a+c>b and b+c>a:
#     print("Треугольник существует")
# else:
#     print("Треугольник с такими сторонами не существует")

# import math
# x = int(input("введите первую координату точки :"))
# y = int(input("введите вторую координату точки :"))
# r = int(input("введите радиус круга :"))
# h = math.hypot(x,y)
# if h<r:
#     print("точка принадлежит кругу")
# else:
#     print("точка не принадлежит кругу")


# a = input("введите строку, состоящую из слов и пробелов :")
# print(a.count(" ")+1)
# print(len(a.split(" ")))

# a = input("введите строку из букв разных регистров :")
# str_1 = ""
# for i in a:
#     if i == i.upper():
#         continue
#     else:
#         str_1+=i
# print(str_1)
#
#
# for i in range(0, 101):
#     if i%7 == 0:
#         continue
#     else:
#         print(i, end=" ")


# summ = 0
# for i in range(0, 101):
#     summ+=i
# print(summ)

# n = int(input("введите число :"))
# pr = 1
# for i in range(1, n+1):
#     pr*= i
# print(pr)

a = ["s", "d", "f", 4, "h", "m", 9]
b = ["k", "l", "s", "d", "j", "s", "g", 9]
str_itog = ""
for i in a:
    if i in b:
        str_itog+= str(i)
print(str_itog)









