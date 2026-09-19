''' Exercício 28: Épossível formar um triângulo?
Leia três medidas positivas e informe se elas podem formar um triângulo.

REGRA:
Três lados formam um triângulo quando cada lado é menor que a soma dos outros dois.

VERIFICAÇÃO FINAL:
Verifique as três desigualdades do triângulo; aprovar apenas uma ou duas comparações não é suficiente.
'''

def traco60():
    print('-'*60)
    print(''' 3 números formam um triângulo? Vamos descobrir!
    Informe 3 números.
\n''')
    print('-'*60)

traco60()

num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo Número: '))
num3 = float(input('Terceiro número: '))

if num1 <= 0 or num2 <= 0 or num3 <= 0: #Verificação para não aceitar números negativos. 
    print(' ERRO: Todas as medidas devem ser POSITIVAS. ')
elif num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2: #Condicionais para verificar a condição de números válidos ou não.
    print(' Os números {0}, {1} e {2} NÃO FORMAM um triângulo. '.format(num1, num2, num3))
else: # ...
    print(' Os números {0}, {1} e {2} FORMAM um triângulo. '.format(num1, num2, num3))
