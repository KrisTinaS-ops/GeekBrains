my_list = ['в', '5', 'часов', '17', 'минут', 'тумпература', 'воздуха', 'была', '+5', 'градусов']

my_list2 = []
for msg in my_list:
    if msg.isdigit():
        my_list2.extend(['"', f'{int(msg):02}', '"'])
    elif msg.startswith('+') and msg[1:].isdigit():
        my_list2.extend(['"', f'{msg[0]}{int(msg[1:]):02}', '"'])
    else:
        my_list2.append(msg)

out_info = ' '.join(my_list2)
print(out_info)