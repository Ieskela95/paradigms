# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Метод сортировки списка пузырьком.
    Попарно сравниваем соседние элементы и меняем местами если правый больше левого.
    В первую итерацию проходим все пары. Затем еще раз. И так, пока список не будет отсортирован"""
    if len(arr) == 0:
        raise ValueError(
            'На вход должен подаваться непустой целочисленный список')
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1):
            if (arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [randint(0, 100) for i in range(10)]
print(numbers)
print(bubble_sort(numbers))
