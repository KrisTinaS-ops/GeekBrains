
with open('nginx_logs.txt') as f:
    qwe = []
    for line in f:
        splitted = line.split()
        qwe.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(qwe)
