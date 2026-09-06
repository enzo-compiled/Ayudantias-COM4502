num = int(input("Numero: "))
for i in range(num, 101):
    if i % num == 0:
        print(i, end= " ")