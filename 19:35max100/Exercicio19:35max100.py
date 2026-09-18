''' Exercício 19: Maior e menor de três números:
Leia três números reais e mostre o maior e o menor valor informado.
O sistema deve funcionar também quando houver valores repetidos.
'''

def maiorNum():
    print('-'*40)
    print(' Informe três números. Vamos descobrir qual é o maior e o menor deles!  ')
    print('-'*40)

maiorNum()

n1 = int(input(' Primeiro valor: '))
n2 = int(input(' Segundo valor: '))
n3 = int(input(' Terceiro valor: '))

if n1 >= n2:
    if n1 >= n3:
        maior = n1
    else:
        maior = n3
else:
    if n2 >= n3:
        maior = n2
    else:
        maior = n3

if n1 <= n2:
    if n1 <= n3:
        menor = n1
    else:
        menor = n3
else:
    if n2 <= n3:
        menor = n2
    else:
        menor = n3
print('Maior: {0}. \nMenor: {1} '.format(maior, menor)) 

#or
# if n1 >= n2 and n1 >= n3:
#     maior = n1
# elif n2 >= n1 and n2 >= n3:
#     maior = n2
# else:
#     maior = n3

# if n1 <= n2 and n1 <= n3:
#     menor = n1
# elif n2 <= n1 and n2 <= n3:
#     menor = n2
# else:
#     menor = n3

# print("Maior: ", maior)
# print("Menor: ", menor)
