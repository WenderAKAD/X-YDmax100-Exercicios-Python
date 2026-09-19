''' Exercício 26: Reajuste por faixa salarial. 
Leia o salário atual e calcule o novo salário conforme a tabela de reajuste. 
REQUISITO:
Mostre o percentual aplicado, o valor do aumento e o novo salário.

REGRAS DO EXERCÍCIO:
Salário atual                  / Reajuste 
Até R$ 1.500,00                / 15%
De R$ 1.500,01 até R$ 3.000,00 / 10%
Acima de R$ 3.000,00           / 5%

VERIFICAÇÃO FINAL:
Teste salários exatamente iguais aos limites das faixas para impedir sobreposição ou ausência de reajuste.'''

def traco60():
    print('-'*60)

traco60()
print('\n Aumento de salário da empresa. Vamos calcular quanto de aumento seu salário terá. ')
print(''' Salários Até R$ 1.500,00 terá um resjuste de 15%.
 De R$ 1.500,01 até R$ 3.000,00 terá um aumento de 10%.
 Acima de R$ 3.000,00 terá um aumento de 5%.
\n''')
traco60()

salarioBase = float(input('\n Seu alário atual: R$ '))

if salarioBase <= 1500:
    aumentoSalario = salarioBase + (salarioBase * 0.15)
    print(' Com o aumento, seu novo salário será de R${0:.2f} '.format(aumentoSalario))
elif 1500.01 <= salarioBase <= 3000:
    aumentoSalario = salarioBase + (salarioBase * 0.10)
    print(' Com o aumento, seu novo salario será de R$ {0:.2f} '.format(aumentoSalario))
elif salarioBase >= 3000.01:
    aumentoSalario = salarioBase + (salarioBase * 0.05)
    print(' Com o aumento, seu novo salário será de R${0:.2f} '.format(aumentoSalario))