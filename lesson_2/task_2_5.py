price = [57.8, 46.51, 97, 45.89, 33, 56.5, 67.55, 40, 77, 0.56]

for price_2 in price:
    rub = int(price_2)
    kk = (price_2 - rub)*100
    print(f'{rub} руб {kk:02.0f} коп')

print()

price = [57.8, 46.51, 97, 45.89, 33, 56.5, 67.55, 40, 77, 0.56]
print(id(price))
price.sort()
print(id(price))

print()

for price_2 in price:
    rub = int(price_2)
    kk = (price_2 - int(price_2))*100
    print(f'{rub} руб {kk:02.0f} коп')

print()

price = [57.8, 46.51, 97, 45.89, 33, 56.5, 67.55, 40, 77, 0.56]

for price_2 in sorted(price)[::-1][:5]:
    rub = int(price_2)
    kk = (price_2 - int(price_2))*100
    print(f'{rub} руб {kk:02.0f} коп')

print()

print([f'{int(price_2)} руб {(price_2-int(price_2))*100:02.0f} коп' for price_2 in sorted(price)[::-1][:5]])
