'''14. Faça um simulador do famoso jogo “leilão do menor valor único”.
Dica: peça ao usuário para fornecer o valor máximo do leilão, em seguida crie um vetor para
armazenar a quantidade de lances para cada valor possível. Para isto dimensione o tamanho do vetor
para 100 vezes o valor máximo do lance (assim ele poderá representar os centavos também).'''

qtde_lance=[]
maior_lance=float(input("Informe o maior lance possível: "))
tam_vet=int(maior_lance*100)
menor_lance=tam_vet+1


for i in range(0,tam_vet):
  qtde_lance.append(0)


valor_lance=int(float(input("Informe o valor do lance: "))*100)
while valor_lance>0 and valor_lance<=tam_vet:

  qtde_lance[valor_lance-1]+=1
  valor_lance=int(float(input("Informe o valor do lance: "))*100)


for i in range(0,tam_vet):
  if qtde_lance[i] == 1 and (i+1)<menor_lance:
    menor_lance=i+1

if menor_lance <= tam_vet:
  print(f"O menor lance vencedor foi R$ {menor_lance/100}")
else:
  print("Não houve lance válido!")