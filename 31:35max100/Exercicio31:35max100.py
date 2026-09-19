''' Exercício 31: Divisível por 3 e por 5: 

Leia um número inteiro e informe em qual situação ele se encontra.

REGRAS DO EXERCÍCIO:

Divisível por 3 e por 5 == DIVISÍVEL POR 3 E 5
Apenas por 3 == DIVISÍVEL APENAS POR 3
Apenas por 5 == DIVISÍVEL APENAS POR 5
Por nenhum dos dois == NÃO DIVISÍVEL POR 3 NEM 5

VERIFICAÇÃO FNIAL
Inclua quatro casos: divisível por ambos, somente por 3, somente por 5 e por nenhum deles

'''

# Exercício 31: Divisível por 3 e por 5

def traco():
    print('-'*60)
    print('''Divisível por 3 e por 5 == DIVISÍVEL POR 3 E 5
Apenas por 3 == DIVISÍVEL APENAS POR 3
Apenas por 5 == DIVISÍVEL APENAS POR 5
Por nenhum dos dois == NÃO DIVISÍVEL POR 3 NEM ''') 
    print('-'*60)

traco()

numero = int(input('Digite um número inteiro: '))

# Verifica a situação usando operadores módulo (%)
if numero % 3 == 0 and numero % 5 == 0:
    resultado = 'DIVISÍVEL POR 3 E 5'
elif numero % 3 == 0:
    resultado = 'DIVISÍVEL APENAS POR 3'
elif numero % 5 == 0:
    resultado = 'DIVISÍVEL APENAS POR 5'
else:
    resultado = 'NÃO DIVISÍVEL POR 3 NEM 5'

print('O número {} se enquadra na situação: {}'.format(numero, resultado))