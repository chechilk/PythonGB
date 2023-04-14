'''## **Task#2**
**Условие:** Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

*Пример:*
* 4 4 -> 2 2
* 5 6 -> 2 3
x + y = b -> y = b - x
x * y = c -> x * (b - x) = c -> (x * b) -(x * -x) - (c * x) = 0
first_number + second_number = summ -> second_number = summ - first_number
first_number + second_number = multi -> first_number * summ -first_number * first_number - multi * first_number

'''
import random
from math import sqrt

first_number = random.randint(0, 21)  # это число Катя должна угадать
second_number = random.randint(0, 21)  # это число Катя должна угадать
print(first_number, second_number)

summ = first_number + second_number
multi = -(first_number * second_number)
print(summ, multi)
disc = summ * summ + 4 * multi

if disc > 0:
    sq = sqrt(disc)
    x1 = -(summ + sq)/(2*(-1))
    x2 = -(summ - sq)/(2*(-1))
    print(int(x2), int(x1))
else:
    print(-1)







