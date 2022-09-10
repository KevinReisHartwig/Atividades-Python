'''12. Leia sexo e idade de uma pessoa e imprima maior idade ou menor idade, considerando que sexo masculino e
maior idade se maior igual a 21 anos e sexo feminino e maior idade se maior igual a 18 anos.'''

sexo = input('digite o sexo da pessoa masculino ou feminina: ')
idade = int(input('digite a idade da pessoa: '))


maior_masc = idade >= 21
maior_fem = idade >= 18
menor_masc = idade < 21
menor_fem = idade < 18

if sexo == "masculino" and maior_masc:
    print("ele é maior de idade tem {} anos de idade".format(idade))

elif sexo == "masculino" and menor_masc:
    print('ele é menor de idade tem {} anos de idade'.format(idade))

elif sexo == "feminina" and maior_fem:
    print('ela é maior de idade tem {} anos de idade'.format(idade))

elif sexo == "feminina" and menor_fem:
    print("ela é menor de idade tem {} anos de idade".format(idade))

else:
    print("você digitou o sexo errado!")
