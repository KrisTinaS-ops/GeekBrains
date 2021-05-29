cube_number = [i**3 for i in range(1,1001,2)]

total = 0

for number in cube_number:
    digit_sum = 0
    temp_number = number
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number = temp_number // 10
    if digit_sum % 7 == 0:
        total += number
print(total)

total_2 = 0
for number in cube_number:
    number += 17
    digit_sum = 0
    temp_number = number
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number = temp_number // 10
    if digit_sum % 7 == 0:
        total_2 += number
print(total_2)