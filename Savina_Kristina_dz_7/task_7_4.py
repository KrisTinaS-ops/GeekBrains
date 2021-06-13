import os

vocab = {}
list_100 = []
list_1000 = []
list_10000 = []
list_100000 = []
list_1000000 = []
for root, dir, files in os.walk(r'C:\Users\ПК\PycharmProjects\GeekBrains'):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size <= 100:
            list_100.append(file)
            vocab[100] = len(list_100)
        elif os.stat(os.path.join(root, file)).st_size <= 1000:
            list_1000.append(file)
            vocab[1000] = len(list_1000)
        elif os.stat(os.path.join(root, file)).st_size <= 10000:
            list_10000.append(file)
            vocab[10000] = len(list_10000)
        elif os.stat(os.path.join(root, file)).st_size <= 100000:
            list_100000.append(file)
            vocab[100000] = len(list_100000)
        else:
            list_1000000.append(file)
            vocab[1000000] = len(list_1000000)

print(vocab)
