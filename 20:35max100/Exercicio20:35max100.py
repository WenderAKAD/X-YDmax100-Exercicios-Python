'''Exercício 20: Três valores em ordem crescente.
Leia três valores inteiros e mostre os valores em ordem crescente. 
REQUISITO: Aceite valores repetidos.
'''

n1 = int(input('Informe o primeiro número : '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 <= n2 and n1 <= n3:
    primeiro = n1

    if n2 <= n3:
        segundo = n2
        terceiro = n3
    else:
        segundo = n3
        terceiro = n2

elif n2 <= n1 and n2 <= n3:
    primeiro = n2

    if n1 <= n3:
        segundo = n1
        terceiro = n3
    else:
        segundo = n3
        terceiro = n1

else:
    primeiro = n3

    if n1 <= n2:
        segundo = n1
        terceiro = n2
    else:
        segundo = n2
        terceiro = n1

print('{0}, {1} e {2}'.format(primeiro, segundo, terceiro))