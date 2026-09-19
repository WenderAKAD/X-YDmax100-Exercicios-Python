''' Exercício 25: Preço conforme a forma de pagamento.
Leia o preço de um produto e a opção de pagamento. Calcule e mostre o valor final conforme a tabela:

Opção / Forma de pagamento / Alteração 
1     / Dinheiro ou PIX    / 10% de desconto
2     / Débito             / 5% de desconto
3     / Crédito à vista    / Sem alteração 
4     / Crédito parcelado  / 8% de acréscimo  

VERIFICAÇÃO FINAL:
Execute uma compra para cada opção de pagamento e confira individualmente o percentual ou acréscimo aplicado.
'''

def traco30(): #Função para ficar mais visualmente agradável. 
    print('-'*40)

traco30() 
print('Calculadora de descontos. ')
traco30()

opcao = int(input(''' Qual será a forma de pagamento? \n 
Opção / Forma de pagamento / Alteração 
1     / Dinheiro ou PIX    / 10% de desconto
2     / Débito             / 5% de desconto
3     / Crédito à vista    / Sem alteração 
4     / Crédito parcelado  / 8% de acréscimo \n 
Opção de pagamento... '''))

valor = float(input(' Informe o valor original: R$'))

if opcao == 1: #10% de desconto.
    desconto = valor - (valor * 0.10)  
    print('\nUm desconto de 10% será aplicado. O valor final a ser pago será de: R${0:.2f} '.format(desconto))
elif opcao == 2: #5% de desconto. 
    desconto = valor - (valor * 0.05) 
    print('\nUm desconto de 5% será aplicado. O valor final a ser pago será de: R${0:.2f} '.format(desconto))
elif opcao == 3: #Sem alteração
    print('\nNa opção de crédito à vista não há desconto. O valor a ser pago se mantém em R${0:.2f}'.format(valor))  
elif opcao == 4: #8% de acréscimo.
    desconto = valor + (valor * 0.08)   
    print('\nCom a opcão de parcelamento no crédito haverá um acréscimo de 8%. O valor total a ser pago será de: R${0:.2f} '.format(desconto))

#ou
# if opcao == 1:
#     valor_final = valor * 0.90  # 10% de desconto
# elif opcao == 2:
#     valor_final = valor * 0.95  # 5% de desconto
# elif opcao == 3:
#     valor_final = valor         # sem alteração
# elif opcao == 4:
#     valor_final = valor * 1.08  # 8% de acréscimo

# print(f'Valor final: R${valor_final:.2f}')