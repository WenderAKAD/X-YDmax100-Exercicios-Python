# Estruturas Condicionais: 
'''Exercício 16: Positivo, Negativo ou Zero. Leia um número real e informe se é positivo, negativo ou se o número é igual a zero. 
'''

def traco40():
    print('-'*40,)

traco40()
print(' Vamos descorbrir se o número é positivo, negativo ou Zero. ')
traco40()


num = int(input('\n Digite um número inteiro: '))
if num < 0:
    print('{0} é negativo.'.format(num))
elif num == 0:
    print('{0} é zero. '.format(num))
elif num > 0:
    print('{0} positivo. '.format(num))
'''    
else:
    print('{0} positivo. '.format(num))
'''

