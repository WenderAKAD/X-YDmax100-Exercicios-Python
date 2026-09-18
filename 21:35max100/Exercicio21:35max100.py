''' Exercício 21: Aprovado ou reprovado
Leia duas notas, calcule a média e informe se o aluno foi aprovado ou reprovado.
REGRA: Para este exercício, média maior ou igual a 7,0 significa APROVADO. Abaixo de 7,0 significa REPROVADO.
'''

def traco40():
    print('-'*40)
    print(''' Vamos calcular a média de duas notas! 
    Média maior que 7.0 == APROVADO;
    Média abaixo de 7.0 == REPROVADO. ''')
    print('-'*40)

traco40()

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

mediaNota = (nota1 + nota2) / 2

print('Sua nota final {0}. '.format(mediaNota))

if mediaNota >= 7:
    print('Aprovado! ')
if mediaNota < 7:
    print('Reprovado! ')

