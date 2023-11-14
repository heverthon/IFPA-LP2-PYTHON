# Questão 4
# Recebe o número de plantas e o número de dias do usuário
numero_plantas = int(input("Digite o número de plantas: "))
numero_dias = int(input("Digite o número de dias: "))

# Calcula a quantidade de água necessária
# Multiplica o número de plantas pelo número de dias e pelo consumo diário de água por planta (0.5 litros por planta por dia)
agua_necessaria = numero_plantas * numero_dias * 0.5

# Exibe o resultado
print("Quantidade total de água necessária (em litros):", agua_necessaria)

'''
A explicação para os alunos seria a seguinte:

1 - O código começa pedindo ao usuário que insira o número de plantas e o número de dias para os quais se deseja calcular a
quantidade de água necessária. As funções inputsão usadas para obter esses valores, que são convertidos em números inteiros
(int) e armazenados nas variáveis numero_plantas​​e numero_dias.

2 - O código calcula a quantidade de água necessária multiplicando o número de plantas pelo número de dias e pelo consumo
diário de água por planta, que é de 0,5 litros por planta por dia. O resultado é armazenado na variável agua_necessaria.

3 - Por fim, o código mostra o resultado, que é a quantidade total de água necessária em litros para atender todas as plantas
durante o período especificado.

Este código é um exemplo prático de como usar variáveis, cálculos matemáticos simples e entrada/saída de dados para resolver
um problema de cálculo de quantidade de água necessária para considerar um número específico de plantas durante um determinado
período de tempo. Pode ser usado para ensinar conceitos de aritmética básica em Python.
'''
