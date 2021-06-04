import requests
from decimal import *


def currency_rates(val):
    val = val.upper()
    way = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in way:
        return None
    money = way[way.find('<Value', way.find(val)) + 7:way.find('</Value>', way.find(val))]
    return f"{(Decimal(money.replace(',', '.')))}"


print(currency_rates('EUR'))
print(currency_rates('USD'))
