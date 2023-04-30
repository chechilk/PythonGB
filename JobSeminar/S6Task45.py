# Найти все пары дружественных чисел
# 220 и 248 - дружественные, так как делите 220 в сумме дают 248, а делители 248 в сумме 220


# Поиск делителей
def find_div(number: int) -> list:
    return [i for i in range(1, number // 2 + 1) if number % i == 0]

checked_set = set()
for i in range(1, 10000):
    sum_i_diveders = sum(find_div(i))
    for j in range(i + 1, 10000):
        if (j == sum_i_diveders and i == sum(find_div(j))):
            print(f'{i} {j}')