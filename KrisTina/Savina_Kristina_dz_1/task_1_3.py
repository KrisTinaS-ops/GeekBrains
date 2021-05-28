num = [i for i in range(1, 21)]

for number in num:
    if number == 1:
        print(number, 'процент')
    elif number <= 4:
        print(number, 'процента')
    else:
        print(number, 'процентов')
