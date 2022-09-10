'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
s1 = int(input("digite o primeiro segmento: "))
s2 = int(input("digite o segundo segmento: "))
s3 = int(input("digite o terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("os segmentos acima forma um triangulo ", end= "")
    if s1 == s2 == s3:
        print("equilátero")
    elif s1 != s2 != s3 != s1:
        print("escaleno")
    else:
        print("isósceles")
else:
    print("não forma um triangulo")

