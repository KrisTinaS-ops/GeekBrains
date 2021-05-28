my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздух', 'была', '+5', 'градусов']

print(my_list.index('5'))
my_list[1] = int('5')
print(type(my_list[1]))
#:02d
print(id(my_list))
my_list.sort()
print(my_list)
print(id(my_list))

my_list[1] = str('5')
print(type(my_list[1]))
my_list.insert(1,'"')
my_list.insert(3,'"')
print(my_list)

print(my_list.index('17'))
my_list.insert(5,'"')
my_list.insert(7,'"')
print(my_list)

print(my_list.index('+5'))
my_list[12] = int('+5')
print(type(my_list[12]))
#:02d
my_list[12] = str('+5')
print(type(my_list[12]))
my_list.insert(12,'"')
my_list.insert(14,'"')
print(my_list)


"""
my_list2 = ' '.join(my_list)
print(my_list2)

"""