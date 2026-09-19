'''Exercício 29: Tipo de triângulo
Leia três medidas. Primeiro verifique se elas formam um triângulo. Se formarem, classifique-o como equilátero, isósceles ou escaleno.

REGRAS DO EXERCÍCIO:
Relação entre os lados / Tipo 
Três lados iguais.    == EQUILÁTERO
Dois lados iguais.    == ISÓSCELES
Três lados diferentes == ESCALENO

VERIFICAÇÃO FINAL:
Tente classificar medidas que não formam um triângulo e confirme que nenhum tipo é informado nesse caso.
'''

def traco60():
    print('-' * 60)
    print(' Três números formam um triângulo EQUILÁTERO, ISÓSCELES OU ESCALENO? Vamos descobrir!')
    print('-' * 60)

traco60()

reta1 = float(input(' Primeiro número: '))
reta2 = float(input(' Segundo número: '))
reta3 = float(input(' Terceiro número: '))

# 1. Validação de medidas positivas
if reta1 <= 0 or reta2 <= 0 or reta3 <= 0:
    print(' ERRO: Todas as medidas devem ser POSITIVAS. ')

# 2. Validação da desigualdade triangular (formam ou não?)
elif reta1 >= reta2 + reta3 or reta2 >= reta1 + reta3 or reta3 >= reta1 + reta2:
    print(' Os números {0}, {1} e {2} NÃO FORMAM um triângulo. '.format(reta1, reta2, reta3))

# 3. Se chegou até aqui, FORMAM um triângulo. Agora classificar!
else:
    print(' Os números {0}, {1} e {2} FORMAM um triângulo.'.format(reta1, reta2, reta3))
    
    # Classificação
    if reta1 == reta2 == reta3:
        print(' Tipo: EQUILÁTERO (Três lados iguais).')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print(' Tipo: ISÓSCELES (Dois lados iguais).')
    else:
        print(' Tipo: ESCALENO (Três lados diferentes).')


# def traco60():
#     print('-' * 60)
#     print(' Três números formam um triângulo EQUILÁTERO, ISÓSCELES OU ESCALENO? Vamos descobrir!')
#     print('-' * 60)

# traco60()

# reta1 = float(input(' Primeiro número: '))
# reta2 = float(input(' Segundo número: '))
# reta3 = float(input(' Terceiro número: '))

# # 1. Validação de medidas positivas
# if reta1 <= 0 or reta2 <= 0 or reta3 <= 0:
#     print(' ERRO: Todas as medidas devem ser POSITIVAS. ')

# # 2. Validação da desigualdade triangular (formam ou não?)
# elif reta1 >= reta2 + reta3 or reta2 >= reta1 + reta3 or reta3 >= reta1 + reta2:
#     print(' Os números {0}, {1} e {2} NÃO FORMAM um triângulo. '.format(reta1, reta2, reta3))

# # 3. Se chegou até aqui, FORMAM um triângulo. Agora classificar!
# else:
#     print(' Os números {0}, {1} e {2} FORMAM um triângulo. '.format(reta1, reta2, reta3))
    
#     # Classificação
#     if reta1 == reta2 == reta3:
#         print(' Tipo: EQUILÁTERO (Três lados iguais).')
#     elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
#         print(' Tipo: ISÓSCELES (Dois lados iguais).')
#     else:
#         print(' Tipo: ESCALENO (Três lados diferentes).')

# def traco60():
#     print('-'*60)
#     print(' Três números formam um triângulo EQUILÁTERO, ISÓSCELES OU ESCALENO? Se sim, qual? Vamos ver! ')
#     print('-'*60)

# traco60()

# reta1 = float(input(' Primeiro número: '))
# reta2 = float(input(' Segundo número: '))
# reta3 = float(input(' Terceiro número: '))

# # Primeiro decisão se os números formam ou não um triângulo:
# if reta1 <= 0 or reta2 <= 0 or reta3 <= 0: #Verificação para não aceitar números negativos. 
#     print(' ERRO: Todas as medidas devem ser POSITIVAS. ')
# elif reta1 > reta2 + reta3 or reta2 > reta1 + reta3 or reta3 > reta1 + reta2: #Condicionais para verificar a condição de números válidos ou não.
#     print(' Os números {0}, {1} e {2} NÃO FORMAM um triângulo. '.format(reta1, reta2, reta3))
# elif: # ...
#     print(' Os números {0}, {1} e {2} FORMAM um triângulo. '.format(reta1, reta2, reta3))

# print(' Entendido, {0}, {1} e {2} não formam um triângulo. ')

# #... Números escolhidos formam um triângulo. Qual tipo de triângulo pode ser formado?
# if reta1 == reta2 == reta3:
#     print(' O triângulo é EQUILÁTERO. ')
