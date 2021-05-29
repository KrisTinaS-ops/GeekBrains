my_list = ['в', '5', 'часов', '17', 'минут', 'тумпература', 'воздуха', 'была', '+5', 'градусов']

my_list2 = []
for elem in my_list:
    if elem.isdigit():
        my_list2.extend(['"', f'{int(elem):02}', '"'])
    elif elem.startswith('+') and elem[1:].isdigit():
        my_list2.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        my_list2.append(elem)

out_info = ' '.join(my_list2)
print(out_info)