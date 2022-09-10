def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mErro: por favor digite um valor inteiro valido\033[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31m o usuario preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("\33[31m você digitou um valor real invalido \033[m")
            continue
        except(KeyboardInterrupt):
            print("\033[31mo usuario não digitou nada \033[m")
            return 0
        else:
            return n



num1 = leiaInt("digite um valor: ")
num2 = leiaFloat("leia um valor real: ")
print(f"o valor digitado é {num1} e {num2}")
