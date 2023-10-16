'''№21. Напишите программу для печати всех уникальных значений в словаре.'''

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
unique_values = set()
for dicts in my_list:  # просматриваем значения словарей в списке
    for value in dicts.values():  # вытаскиваем значения из словаря
        unique_values.add(value)
print(unique_values)
#   вариант решения 2
for dicts in my_list:
    for key, value in dicts.items():
        unique_values.add(value)
print(unique_values)
