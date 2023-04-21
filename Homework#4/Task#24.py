import random

number_of_beds = int(input('Enter number of beds: '))

beds_list = list()
count_berries = list()

for i in range(number_of_beds):
    beds_list.append(random.randint(1, 25))
print(beds_list)
for i in range(len(beds_list) - 1):
    count_berries.append(beds_list[i] + beds_list[i + 1] + beds_list[i - 1])

print(max(count_berries))
