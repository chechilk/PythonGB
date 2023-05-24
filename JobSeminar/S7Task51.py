# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику


# print(list(map((lambda x: True if len(x) > 5 else False), my_list)))
# print(bool(map((lambda x: True if len(x) > 5 else False), my_list)))


def same_by(characteristic, objects) -> bool:
    return len(set(map(characteristic, objects))) <= 1


my_list = [2, 4, 6, 8]
print(same_by(lambda x: x % 2, my_list))
