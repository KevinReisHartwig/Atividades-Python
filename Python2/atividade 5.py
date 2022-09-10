'''5) Faça um algoritmo que leia a altura de moças inscritas em um concurso de beleza. Para
finalizar será digitado zero na altura. Imprima as duas maiores alturas.'''

# fazer um algoritimo que leia a altura e finalizar digitando zero na altura e imprima as duas maiores alturas:

cont = 0
maior = 0
maior2 = 0

altura = float(input("digite a altura para parar digite 0: "))

while altura != 0:
  cont = cont + 1
  if altura > maior:
    maior2 = maior
    maior = altura
  elif altura > maior2 and altura != maior:
    maior2 = altura

  altura = float(input("digite a altura para parar digite 0: "))

if(cont == 0):
  print("Não houveram candidatas inscritas!")
elif(cont == 1):
  print("Apenas uma candidata inscrita. Altura: ",maior)
else:
  print("Maior altura: ",maior, "\nSegunda maior altura: ", maior2)



