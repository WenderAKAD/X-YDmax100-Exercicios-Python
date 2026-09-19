''' Exercício 27: Classificação de IMC
Leia o peso em quilogramas e a altura em metros. Calcule o IMC e classifique o resultado usando apenas as regras didáticas da tabela.

REGRAS DO EXERCÍCIO:
IMC
Menor que 18,5.                        ==   ABAIXO DA FAIXA
Maior ou igual a 18,5 e menor que 25,0 ==   FAIXA NORMAL
Maior ou igual a 25,0 e menor que 30,0 ==   ACIMA DA FAIXA
Maior ou igual a 30,0                  ==   FAIXA ELEVADA
'''

def traco60():
    print('-'*60)
    print(' Cálculo de IMC! ')
    print('''Menor que 18,5.                        ==   ABAIXO DA FAIXA
Maior ou igual a 18,5 e menor que 25,0 ==   FAIXA NORMAL
Maior ou igual a 25,0 e menor que 30,0 ==   ACIMA DA FAIXA
Maior ou igual a 30,0                  ==   FAIXA ELEVADA
''')
    print('-'*60)
    
# Leitura da altura
altura_input = float(input("Informe sua altura (em metros ou centímetros): "))

# O. usuário pode digitar sua altutra em metros "175 cm" ou em metros "1.75" e para isso é necessário corrigir.
# Verificação inteligente para converter cm para m se necessário 
if altura_input > 3:
    # Se for maior que 3, assumimos que o usuário digitou em cm
    altura = altura_input / 100
    print(f"Atenção: Altura convertida de {altura_input} cm para {altura} m.")
else:
    # Se for menor ou igual a 3, assumimos que já está em metros
    altura = altura_input

# Leitura do peso
peso = float(input("Informe seu peso em kg: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação
if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")


