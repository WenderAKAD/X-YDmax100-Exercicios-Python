# Estruturas Condicionais: 
'''Exercício 16: Positivo, Negativo ou Zero. Leia um número real e informe se é positivo, negativo ou se o número é igual a zero. 
'''
num = int(input(' Digite um número inteiro: '))
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

