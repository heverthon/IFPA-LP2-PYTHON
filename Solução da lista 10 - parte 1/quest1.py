#Questão1
'''
1. Nutrição:
Problema: Um nutricionista precisa calcular o Índice de Massa Corporal (IMC) de um
paciente. O IMC é calculado dividindo o peso do paciente (em kg) pela altura ao quadrado
(em metros).
Exercício: Escreva um algoritmo que receba o peso e a altura de um paciente, calcule e exiba
o IMC.

'''


# Solicita ao usuário que insira o peso do paciente em quilogramas e armazena o valor em uma variável 'peso'.
peso = float(input("Digite o peso do paciente em kg: "))

# Solicita ao usuário que insira a altura do paciente em metros e armazena o valor em uma variável 'altura'.
altura = float(input("Digite a altura do paciente em metros: "))

# Calcula o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura^2) e armazena o resultado na variável 'imc'.
imc = peso / (altura ** 2)

# Imprime o valor do IMC, arredondado para 2 casas decimais, para o usuário.
print("O índice de Massa Corporal (IMC) é: ", round(imc, 2))

'''

A explicação para os alunos seria a seguinte:

1 - O código começa solicitando que o usuário insira o peso do paciente em quilogramas e a altura em metros. As funções input são
usadas para obter os valores digitados pelo usuário.

2 - Os valores digitados são convertidos em números de ponto flutuante (float) e armazenados nas variáveis peso ​​e altura.

3 - Em seguida, o código calcula o Índice de Massa Corporal (IMC) usando a fórmula padrão, que é IMC = peso / (altura^2). O resultado
é armazenado na variável imc.

4 - Finalmente, o IMC é impresso na tela, arredondado para duas casas decimais, para fornecer uma leitura mais legível.

Este código é um exemplo simples de como os conceitos de entrada de dados, cálculos matemáticos e saída de resultados podem ser
aplicados em Python. O IMC é uma medida comum usada na área de saúde para avaliar o estado de saúde com base no peso e na altura
de uma pessoa. Ele pode ser usado como um exemplo prático para ensinar conceitos básicos de entrada e saída de dados, operações
matemáticas e formatação de saída em Python.

'''
