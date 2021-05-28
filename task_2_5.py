price = [57.8, 46.51, 97, 55, 37.33, 17.06, 87.92, 66, 23.7, 78]
#A вывод в виде 57 руб. 08 коп



#B сортировка по возрастанию
print(id(price))
price.sort()
print(id(price))
print(price)

#C новый список по убыванию
price_2 = price[::-1]
print(price_2)

#D вывод 5-ти самых больших
print(price_2[:5])