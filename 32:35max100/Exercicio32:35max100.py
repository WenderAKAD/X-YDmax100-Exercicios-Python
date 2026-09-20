''' Exercício 32: Número dentro do intervalo
Leia um número real e informe se ele está dentro do intervalo fechado de 10 até 20.

REGRA:
Os valores 10 e 20 pertencem ao intervalo.

VERIFICAÇÃO FINAL
Teste exatamente 10 e 20; como o intervalo é fechado, os dois limites devem ser considerados internos. '''

# Exercício 32: Número dentro do intervalo

def traco60():
    print('-'*60)
    print(' Vamos ler um número e verificar se ele está ou não em um intervalo entre20 10 e 20. ')
    print('-'*60)

traco60()

numero = float(input('Digite um número real: '))

# Verifica se o número está no intervalo fechado [10, 20]
# A regra diz que 10 e 20 pertencem ao intervalo (<= e >=)
if numero >= 10 and numero <= 20:
    situacao = 'DENTRO do intervalo [10, 20]'
else:
    situacao = 'FORA do intervalo [10, 20]'

print('O número {} está {}'.format(numero, situacao))