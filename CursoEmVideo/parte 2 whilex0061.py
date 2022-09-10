print("Gerador de Pa")
print("-="*10)
primeiro = int(input("digite o primeiro termo: "))
razão = int(input("digite a razão PA: "))
termo = primeiro
cont = 1

while cont <= 10:
    print("{} ->".format(termo),end='')
    termo = termo + razão
    cont = cont + 1
print("fim")