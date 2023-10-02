# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

MAX_WEIGHT = 10
stuff = {'Палатка': 5, 'Спальник': 2, 'Пенка': 0.5, 'Аптечка': 0.3,
         'Планшет': 0.3, 'Одежда': 0.5, 'Компас': 0.1, 'Еда': 1, 'Вода': 1.5, 'Нож': 0.2}


def fill_backpack(items_to_pack):
    packed_items = {}
    current_weight = 0
    for item, weight in items_to_pack.items():
        if current_weight + weight <= MAX_WEIGHT:
            packed_items[item] = weight
            current_weight += weight
    return packed_items


print(fill_backpack(stuff))
