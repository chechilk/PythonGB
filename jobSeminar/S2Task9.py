'''По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 '''

number = int(input('Введите число: '))

fact = 1
i = 1
while i <= number:
    fact *= i
    i += 1

# for i in range(1,  number + 1):
#     fact *= 1

print(fact)