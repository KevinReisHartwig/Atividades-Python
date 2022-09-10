'''12)Faça um algoritmo que leia a altura e o sexo de n pessoas e imprima:
a) - Quantos homens e mulheres foram medidas;
b) - Quantos homens acima de 1,70;
c) - A média das alturas das mulheres.
OBS: O número n de pessoas será fornecida pelo usuário do programa no início da sua
execução.'''

n = int(input("digite o numero de pessoas: "))

homem = 0
mulher = 0
homem_170 = 0
soma_mulher = 0

for i in range(n):
    sexo = input("digite o sexo masculino = M ou feminino = F: ").lower()

    while sexo != 'm' and sexo != 'f':
        sexo = input("valor invalido informe o sexo novamente masculino = M ou feminino = F: ")
    altura = float(input("digite a altura: "))

    if sexo == 'm':
      homen = homem + 1
      if altura > 1.70:
        homem_170 = homem_170 + 1
    elif sexo == 'f':
      mulher = mulher + 1
      soma_mulher = soma_mulher + altura
media = soma_mulher / mulher
print("Quantidades de mulheres: ", mulher)
print("Quantidades de homens: ", homem)
print("Quantidades de homens acima de 1.70 metros: ", homem_170)
print("Médias das alturas das mulheres: {:.2f} ".format(media))