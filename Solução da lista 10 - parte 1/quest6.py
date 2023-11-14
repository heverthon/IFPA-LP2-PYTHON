#Questão 6
# Recebe o número de kWh consumidos do usuário
kwh_consumidos = float(input("Digite o número de kWh consumidos: "))

# Define o custo por kWh
custo_por_kwh = 0.50

# Calcula o custo total da energia elétrica
custo_total = kwh_consumidos * custo_por_kwh

# Exibe o resultado
print("Custo mensal de energia elétrica: R$", round(custo_total, 2))

'''
A explicação para os alunos seria a seguinte:

1 - O código começa pedindo ao usuário que insira o número de quilowatts-hora (kWh)
consumidos no mês. A função inputé usada para obter esse valor, que é convertida em
um número de ponto flutuante e armazenado na variável kwh_consumidos.

2 - O código define o custo por kWh, que é de R$0,50 por kWh, e armazena esse valor
na variável custo_por_kwh.

3 - Em seguida, o código calcula o custo total da energia elétrica multiplicando o número
de kWh consumidos pelo custo por kWh. O resultado é armazenado na variável custo_total.

4 - Por fim, o código exibe o resultado, que é o custo mensal de energia elétrica em reais
(R$), formatado com duas casas decimais, usando a função round(custo_total, 2).

Este código é um exemplo prático de como usar variáveis, cálculos matemáticos e entrada/saída
de dados para calcular o custo mensal de energia elétrica com base no consumo de kWh. Pode
ser usado para ensinar conceitos de cálculos financeiros simples em Python, especialmente
relacionados ao uso de energia elétrica.
'''
