''' Exercício 18: Leia dois números reais e mostre qual deles é o maior. Se os dois valores forem iguais, informe que não existe valor maior.
'''
print(' Vamos descobrir qual é o maior valor. ')
valor_1 = int(input(' Digite um número: '))
valor_2 = int(input(' digite outro número: '))

if valor_1 > valor_2:
    print(' O maior número é {0} '.format(valor_1))
elif valor_2 > valor_1:
    print(' O maior valor é {0} '.format(valor_2))
else:
    print(' Os valores são iguais. ')