''' Exercício 24: Ano bissexto.
Leia um número inteiro e informe se ele é bissexto.
REGRA:
Um ano é bissexto quando é divisível por 400, ou quando é divisível por 4 e não é divisível por 100.
'''

def traco50():
    print('-'*50)
    print(' Vamos descobrir se o ano é bissexto ou não! ')
    print('-'*50)
    
traco50()

ano = int(input('Informe o ano: '))

if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0: #Cálculo para verificar se o ano é bissexto. 
    print(f'O ano {ano} é bissexto. ')
else: #Se não for...
    print(f'O ano {ano} não é bissexto. ')