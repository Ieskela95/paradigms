# Написать программу на Python в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

# Реализуем программу в императивной парадигме. Для начала, создаем функцию бинарного поиска:
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Используем
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, x)

if result != -1:
    print(f"Элемент найден в индексе {result}.")
else:
    print("Элемент не найден в массиве.")
