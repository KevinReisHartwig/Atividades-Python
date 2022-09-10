def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\33[31mdigite um valor valido!\33[m")
        if ok:
            break
    return valor

n = leiaInt("digite um valor: ")
print(f"você digitou o valor {n}")