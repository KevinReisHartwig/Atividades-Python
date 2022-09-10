'''3. Leia um conjunto de salários, sendo que para terminar a entrada será fornecido o valor -1. Após toda
a entrada ter sido realizada, leia o valor de um reajuste. Em seguida exiba todos os salários já
reajustados. '''

salarios = []
reajuste = []
reajuste2 = 0
quantidade = 0
salario = float(input("digite os salarios para finalizar digite -1: "))
if salario != -1:
    salarios.append(salario)
while salario != -1:
    salario = float(input("digite o salario: "))
    quantidade = quantidade + 1

    if salario != -1:
        salarios.append(salario)
print("os salarios são {}".format(salarios))
for i in range(quantidade):
    reajuste2 = salarios[i] + (salarios[i] * 0.10)
    reajuste.append(reajuste2)

print("o reajuste de 10% é {}".format(reajuste))
print(quantidade)


