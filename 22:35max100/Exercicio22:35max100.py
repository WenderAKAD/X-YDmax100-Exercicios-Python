''' Exercício 22: Situação do aluno por faixa.
Leia duas notas, calcule a média e informe a situação do aluno conforme a tabela.

REGRAS DO EXERCÍCIO Média
Menor que 5,0
Maior ou igual a 5,0 e menor que 7,0 Maior ou igual a 7,0

'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

mediaNota = (n1 + n2) / 2

print(f'Nota 1: {n1}')
print(f'Nota 2: {n2}')
print('Sua média é {0:.2f} '.format(mediaNota))

#Estou desconsiderando valores negativos e acima de 10 por conta da proposta de testar a ideia de exercício de condicionais.
if mediaNota < 5:
    print('Reprovado! ')
elif mediaNota <= 5 or mediaNota < 7:
    print('Recuperação! ')
elif mediaNota >= 7:
    print('Aprovado! ')

