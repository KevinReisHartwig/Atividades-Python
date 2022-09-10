'''Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
medida = int(input("digite a medida em metros: "))
cm = medida * 100
mm = medida * 1000
print("a medida {} tem {} cm e {} mm".format(medida,cm,mm))