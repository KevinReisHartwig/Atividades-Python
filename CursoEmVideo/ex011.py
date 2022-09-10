'''Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

altura = float(input("digite a altura da parede: "))
largura = float(input("digite a largura da parede: "))
metros = altura * largura
print("para sabermos o metro quadrado da parede basta fazer {} X {} que vai dar {} m²".format(altura, largura, metros))
tinta= metros/2
print("ele vai precisar de {}L de tinta para pintar a parede".format(tinta))
