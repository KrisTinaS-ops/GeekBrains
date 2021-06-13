#show_sales
import sys
from itertools import islice

command_list = [*sys.argv]

if len(command_list) == 1:
    with open('bakery.csv', encoding='utf-8') as f:
        print(f.read())

#без чтения всего файла
if len(command_list) == 2:
     number = int(command_list[1])-1
     with open('bakery.csv', encoding='utf-8') as f:
         out_info = list(islice(f, number, None))
         print(''.join(out_info))

if len(command_list) == 3:
     number1 = int(command_list[1])-1
     number2 = int(command_list[2])
     with open('bakery.csv', encoding='utf-8') as f:
         out_info = list(islice(f, number1, number2))
         print(''.join(out_info))
