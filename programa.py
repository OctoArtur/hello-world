num = int(input("Digite um número natural: "))
if num <= 1:
    print(f"{num} NÃO é primo.")
for i in range(num - 1, 0, -1):
    print (i)
    if i == 1:
        print(f"{num} é primo.")
        break
    if num % i == 0:
        print(f"{num} NÃO é primo.")
        break