'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

print("{:=^40}".format("\33[31m Lojas KevinReis \33[m"))
gasto = float(input("Preço das compras:"))
print('''formas de pagamento:"
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2X no cartão
[4] 3X ou mais no cartão''')
opção= int(input("digite qual opção: "))
if opção == 1:
    total = gasto - (gasto*0.10)
elif opção == 2:
    total = gasto - (gasto*0.5)
elif opção == 3:
    total = gasto
    parcela = gasto/2
    print("sua compra vai ser parcelada em 2x de R${}".format(parcela))
elif opção == 4:
    total = gasto + (gasto * 0.20)
    total_parc = int(input("quantas parcelas: "))
    parcelas = total / total_parc
    print("você parcelou em {:.2f}x de R${:.2f}".format(total_parc,parcelas))
else:
    total = gasto
    print("\33[31mOpção invalida!\33[m")
print("sua compra de R${:.2f} vai custar R${:.2f} no final".format(gasto,total))
