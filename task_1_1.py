duration = int(input('Ведите продолжительность времени в секундах: '))

min = 60
hour = 3600
day = 86400

if duration < min:
    print(duration, 'сек')
elif duration < hour:
    m = duration // min
    s = duration % min
    print(m, 'мин', s, 'сек')
elif duration < day:
    h = duration // hour
    m = duration % hour // min
    s = duration % hour % min
    print(h, 'час', m, 'мин', s, 'сек')
else:
    d = duration // day
    h = duration % day // hour
    m = duration % day % hour // min
    s = duration % day % hour % min % min

    print(d, 'дн' , h, 'час', m, 'мин', s, 'сек')