''' Exercício 23: Categoria de votação.
Leia a idade de uma pessoa e informe a categoria de votação conforme as regras didáticas da tabela.

REGRAS DO EXERCÍCIO:
Menor de 16 NÃO PODE VOTAR;
16 ou 17 VOTO OPCIONAL;
De 18 a 60 anos VOTO OBRIGATÓRIO;
70 anos ou mais VOTO OPCIONAL.
'''

idade = int(input('Informe sua idade: '))

if idade < 16:
    print('Menores de 16 anos não podem votar. ')
elif 16 >= idade and idade <= 17:
    print('Você tem {0} anos. Voto opcional. '.format(idade))
elif idade >= 18 and idade <= 69:
    print('Voto obrigatório. ')
elif idade > 69:
    print('Voto opcional. ')
