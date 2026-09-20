''' Exercício 35: Valor do Ingresso. 
O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é estudante. Calcule o valor final conforme as regras.

REGRA:
Paga meia-entrada quem tiver menos de 12 anos, quem for estudante ou quem tiver 60 anos ou mais. O desconto é de 50% e não é acumulativo. 

TESTE SEU PROGRAMA:
Idade / Estudante / Valor esperado
10.   / NÃ0.      / R$ 15,00
25.   / SIM.      / R$ 15,00
65.   / NÃ0.      / R$ 15,00
30.   / NÃ0.      / R$ 30,00 

VERIFICAÇÃO FINAL:
Teste alguém que satisfaça mais de uma condição de meia-entrada e confirme
que o desconto de 50% não é acumulado. '''

def traco60():
    print('-'*60)
    print('   SISTEMA DE VALOR DE INGRESSO')
    print('   Regras de Meia-Entrada')
    print('-'*60)

traco60()

# Exercício 35: Valor do Ingresso

preco_original = 30.00

idade = int(input('Digite sua idade: '))
estudante_input = input('Você é estudante? (sim/não): ').strip().lower()

# Converte a resposta do estudante para booleano
# Considera 'sim', 's', 'y', 'yes' como verdadeiro, e 'não', 'nao', 'n' como falso
if estudante_input in ['sim', 's', 'y', 'yes']:
    e_estudante = True
else:
    e_estudante = False

# Regra: Paga meia-entrada se tiver < 12 anos, for estudante OU tiver >= 60 anos
# O desconto não é acumulativo (se satisfaz mais de uma, o desconto continua sendo 50%)
if idade < 12 or e_estudante or idade >= 60:
    valor_final = preco_original * 0.5
    condicao = 'meia-entrada'
else:
    valor_final = preco_original
    condicao = 'inteira'

# Mostrar o resultado.
print('Idade: {} anos'.format(idade))
print('Estudante: {}'.format('Sim' if e_estudante else 'Não'))
print('Situação: {}'.format(condicao))
print('Valor a pagar: R$ {:.2f}'.format(valor_final))