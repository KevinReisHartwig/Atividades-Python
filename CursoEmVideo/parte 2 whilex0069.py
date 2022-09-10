'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
tot18 = quantH = mulher20 = 0
while True:
    idade = int(input("digite a idade : "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("digite seu sexo F/M: ")).strip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == "M":
        quantH += 1
    if sexo == "F" and idade >= 20:
        mulher20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("digite sim ou não para continuar: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"teve {tot18} pessoas maiores de 18")
print(f"teve {quantH} homens")
print(f"teve {mulher20} mulheres maiores de 20 anos")
