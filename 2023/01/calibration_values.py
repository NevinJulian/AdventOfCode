import re

with open('input2.txt', 'r') as file:
    lines = file.readlines()

numbers_in_text = []

for line in lines:
    numbers_in_text.append(re.findall(r'\d', line))

first_and_last_pair = []

for number in numbers_in_text:
    first_and_last_pair.append(int(str(number[0]) + str(number[-1])))

print(sum(first_and_last_pair))