''' Exercício 34: Quantidade de dias do mês.
Leia o número de um mês e um ano. Mostre quantos dias o mês possui.

REGRA:
Meses 1, 3, 5, 7, 8, 10 e 12 possuem 31 dias. Meses 4, 6, 9 e 1 possuem 30 dias.
Fevereiro possui 28 dias, ou 29 em ano bissexto.

REQUISITO:
Se o mês estiver fora de 1 a 12, mostre MÊS INVÁLIDO. 

VERIFICAÇÃO FINAL:
Confira fevereiro em um ano comum e em um ano bissexto, além de um mês com 30 e outro com 31 dias.'''

def traco60():
    print('-'*60)  
    print(' Digite um número inteiro. Vamos descobrir se o número escolhido equivale a um mês do ano. ')  
    print('-'*60)    

traco60()

# Exercício 34: Quantidade de dias do mês

mes = int(input('Digite o número do mês (1 a 12): ')) # mês e ano não aceitam valores float.
ano = int(input('Digite o ano: '))

# Verificação inicial: se o mês estiver fora de 1 a 12
if mes < 1 or mes > 12:
    print('MÊS INVÁLIDO')
else:
    # Determinar se é ano bissexto
    # Um ano é bissexto se for divisível por 4, exceto se for divisível por 100, a menos que seja divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    # Determinar a quantidade de dias
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes in [4, 6, 9, 11]:
        dias = 30
    elif mes == 2:
        if bissexto:
            dias = 29
        else:
            dias = 28
    else: # Precaução para caso o usuário decida colocar dias = 0.
        dias = 0

    # Verificação: se o mês for inválido, dias será 0 para não influenciar no código.
    if dias > 0:
        print('O mês {} do ano {} possui {} dias.'.format(mes, ano, dias))