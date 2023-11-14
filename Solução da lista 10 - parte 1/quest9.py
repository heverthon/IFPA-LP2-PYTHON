#Questão 9
# Recebe o peso do paciente do usuário
peso_paciente = float(input("Digite o peso do paciente em kg: "))

# Calcula a dosagem do medicamento
dosagem = peso_paciente  # 1mg por kg de peso

# Exibe o resultado
print("A dosagem do medicamento é:", dosagem, "mg")

'''
A explicação para os alunos seria a seguinte:

1. O código começa solicitando ao usuário que insira o peso do paciente em quilogramas.
A função `input` é usada para obter esse valor, que é convertido em um número de ponto
flutuante (float) e armazenado na variável `peso_paciente`.

2. O código calcula a dosagem do medicamento simplesmente atribuindo o valor do peso
do paciente à variável `dosagem`. A lógica utilizada é de 1mg por kg de peso.

3. Por fim, o código exibe o resultado, que é a dosagem do medicamento em miligramas
(mg), usando a função `print`.

Este código é um exemplo prático de como usar entrada de dados, variáveis e cálculos
matemáticos simples para calcular a dosagem de um medicamento com base no peso do
paciente. Pode ser usado para ensinar conceitos de entrada/saída de dados e cálculos
básicos em Python.
'''
