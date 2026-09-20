''' Exercício 33: Dia da semana. 
Leia um número de 1 a 7 e mostre o dia da semana correspondente. Para qualquer outro valor, mostre OPÇÃO INVÁLIDA.

TABELA DE REFERÊNCIA:
1 == Segunda-feira 
2 == Terça-feira
3 == Quarta-feira
4 == Quinta-feira
5 == Sexta-feira
6 == Sábado
7 == Domingo

VERIFICAÇÃO FINAL:
Use 0 e 8 para confirmar que valores fora de 1 a 7 produzem a mensagem de opção inválida.'''

def traco60():
    print('-'*60)
    print(' Digite um número entre 1 e 7 e o programa mostrará qual dia da semana o número escolhido equivale.  ')
    print('-'*60)

traco60()

# Exercício 33: Dia da semana

numero = int(input('Digite um número de 1 a 7: '))

# Mapeamento dos dias da semana
if numero == 1:
    dia = 'Segunda-feira'
elif numero == 2:
    dia = 'Terça-feira'
elif numero == 3:
    dia = 'Quarta-feira'
elif numero == 4:
    dia = 'Quinta-feira'
elif numero == 5:
    dia = 'Sexta-feira'
elif numero == 6:
    dia = 'Sábado'
elif numero == 7:
    dia = 'Domingo'
else:
    dia = None

# Verificação final: se o dia for None, significa que a opção é inválida
if dia is None:
    print('OPÇÃO INVÁLIDA. ')
else:
    print('O dia correspondente ao número {} é: {}'.format(numero, dia))
