# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from math import pi

d = int(input("Введите целое число для заданной точности числа Пи после запятой:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# # Формула Бэйли — Боруэйна — Плаффа
# import math
# from math import pi

# n = pi
# print(n)



# n = 100
# my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
# print(my_pi)



# # Ряд Лейбница

# n = 20000000

# mypi = 4 * (sum(1/x for x in range(1, n + 1, 4)) + sum(-1/x for x in range(3, n + 1, 4)))

# print(format(mypi, '.100'))



# формула Чудновского

# from math import factorial as fact
# i = 1
# sgn = -1
# a = 13591409
# b = 545140134
# c = 640320
# d = c ** (3/2)
# s = a / d 
# ss = 3
# while str(ss)[:12] != '3.1415926535' :
#     tmp = (sgn * fact(6*i) * (a + b*i) / 
#     (fact(3*i) * fact(i) ** 3 * d * c**(3*i)))
#     s += tmp
#     sgn *= -1
#     i += 1
#     ss = 1 / (12*s)
# print(ss)