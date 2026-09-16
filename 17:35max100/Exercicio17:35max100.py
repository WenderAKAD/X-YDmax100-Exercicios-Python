'''Exercício 17: Par ou ímpar. - Leia um número inteiro e informe se ele é par ou ímpar. 
'''

def traco40():
    print('-'*60,)

traco40()
print('Vamos verificar se o valor é PAR ou ÍMPAR! ')
traco40()


num = int(input(' Digite um número inteiro: '))

if num % 2 == 0:
    print(' {0} é um número par'.format(num))
elif num % 2 == 1:
    print(' {0} é um número ímpar. '.format(num))


