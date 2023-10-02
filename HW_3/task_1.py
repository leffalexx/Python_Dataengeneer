# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for el in input_list:
        if el in seen:
            duplicates.add(el)
        else:
            seen.add(el)
    return list(set(duplicates))


my_list = [1, 2, 1, 2, 1, 2, 3, 3, 3, 4, 0, 8, 1]
print(my_list)
print(find_duplicates(my_list))
