# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

lst =[randint(0,10) for i in range(randint(3,10))]
print(lst, "\n")
lst2 = set(lst)
print(list(lst2))