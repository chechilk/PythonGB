# Работа на семинарах.
# Семинар 2
### S2Task9

**Условие:** По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while.
* Input: 5
* Output: 120

### S2Task11
**Условие:** Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
* Input: 5
* Output: 6

### S2Task13
**Условие:** Сколько дней длилась самая длинная оттепель. Оттепель, где градусы > 0.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50.
* Input: 6 -> -20 30 -40 50 10 -10
* Output: 2

### S2Task15
**Условие:** Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза.
* Input: 5 ->  5 1 6 5 9
* Output: 1 9
# Семинар 3
### S3Task17
**Условие:** Дан список чисел. Определите, сколько в нем
встречается различных чисел.
* Input: [1, 1, 2, 0, -1, 3, 4, 4]
* Output: 6

### S3Task19 
**Условие:** Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
* Input: [1, 2, 3, 4, 5] k = 3
* Output: [4, 5, 1, 2, 3]

### S3Task21
**Условие:** Напишите программу для печати всех уникальных
значений в словаре.
* Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
* Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Семинар 4
### S4Task25
**Условие:** Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
* Input: a a a b c a a d c d d
* Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

### S4Task27
**Условие:** Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
* Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
* Output: 13
# Семинар 5
## S5Task31
**Условие:** Последовательностью Фибоначчи называется
последовательность чисел, где а1 = 0, а2 = 1, а3 = а1 + а2
Требуется найти N-е число Фибоначчи

n −10 −9 −8  −7 −6 −5 −4 −3 −2 −1 0 1 2 3 4 5 6 7  8  9  10

F −55	34 −21 13 −8  5  3	2 −1  1 0 1 1 2 3 5 8 13 21 34 55

## S5Task33 
**Условие:** Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
* Input: 5 -> 1 3 3 3 4
* Output: 1 3 3 3 1

## S5Task35
**Условие:** Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. Простое число - это число, которое имеет 2 делителя: 1 и n(само число).

## S5Task37 
**Условие:** Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
* Input: 2 -> 3 4
* Output: 4 3
# Семинар 6
## S6Task39
**Условие:** Даны два списка чисел. Требуется вывести те элементы
первого списка (в том порядке, в каком они идут в первом
списке), которых нет во втором списке. Пользователь вводит
число N - количество элементов в первом списке, затем N
чисел - элементы списка. Затем число M - количество
элементов во втором списке. Затем элементы второго списка.

* Input: 7 -> 3 1 3 4 2 4 12 | 6 -> 4 15 43 1 15 1
* Output: 3 3 2 12

## S6Task41 
**Условие:** Дан список, состоящий из целых чисел. Напишите
программу, которая в данном списке определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в списке
Далее записаны N чисел — элементы списка. Список
состоит из целых чисел.

## S6Task43
**Условие:** Дан список чисел. Посчитайте, сколько в нём пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.

## S6Task45
**Условие:** Найдите все пары дружественных чисел до 10 000.

## S7Task47
**Условие:** У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать): 

transformation = <???> # или любой другой список

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 

transormed_values = list(map(transformation, values))

Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values

## S7Task49
**Условие:** # Дан кортеж, задача определить площадь какой пары будет максимальной. S = pi*a*b, где a и b - длины полуосей эллипса. 

find_farthest_orbit(list_of_orbits)
