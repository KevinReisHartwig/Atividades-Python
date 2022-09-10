"""4. Uma empresa concederá um aumento de salário aos seus funcionários, que varia de acordo com o cargo,
conforme a tabela. Faça um algoritmo que leia o salário e o código do cargo de um funcionário e calcule o novo
salário. Se o cargo do funcionário não estiver na tabela, ele deverá receber 5% de aumento. Imprima o salário
antigo, o novo salário e a diferença. (utilize a estrutura ESCOLHA)
Código do Cargo Percentual
101 (Gerente) 10%
102 (Engenheiro) 20%
103 (Técnico) 30%"""

cargo = int(input("escreva seu codigo do cargo cargo: "))
salario = float(input("digite seu salario: "))

if cargo == 101:
    print("seu novo salario é de {:.2f}".format(salario+(salario*0.10)))
elif cargo == 102:
    print("seu novo salario é de {:.2f}".format(salario+(salario*0.20)))
elif cargo == 103:
    print("seu salario novo é de {:.2f}".format(salario+(salario*0.30)))
else:
    print("seu salario novo é de {:.2f}".format(salario+(salario*0.05)))



