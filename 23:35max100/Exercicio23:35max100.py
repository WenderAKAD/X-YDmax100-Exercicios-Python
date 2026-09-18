''' Exercício 23: Categoria de votação.
Leia a idade de uma pessoa e informe a categoria de votação conforme as regras didáticas da tabela.

REGRAS DO EXERCÍCIO:
Menor de 16 NÃO PODE VOTAR;
16 ou 17 VOTO OPCIONAL;
De 18 a 60 anos VOTO OBRIGATÓRIO;
70 anos ou mais VOTO OPCIONAL.
'''

def traco50():
    print('-'*50)
    print(' \n Verificação de idade para a votação. ')
    print('-'*50)

traco50()

idade = int(input('Informe sua idade: '))

if idade < 16:
    print('Menores de 16 anos não podem votar. ')
elif 16 >= idade or idade <= 17:
    print('Você tem {0} anos. Voto opcional. '.format(idade))
elif 18 <= idade <= 69:
    if idade <= 69:
        print('Você tem {0} anos. Voto obrigatório. '.format(idade))
elif idade >= 70:
    print('Você tem {0} anos. Voto opcional. '.format(idade))
 
