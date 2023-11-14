#Questão 5
# Recebe a distância da viagem em quilômetros do usuário
distancia_km = float(input("Digite a distância da viagem em km: "))

# Define o custo do combustível por quilômetro (0.1 litros por quilômetro a R$5,00 por litro)
custo_por_km = 0.1 * 5.00

# Calcula o custo total da viagem
custo_total = distancia_km * custo_por_km

# Exibe o resultado
print("Custo total do combustível: R$", round(custo_total, 2))

'''
A explicação para seus alunos seria a seguinte:

1 - O código começa pedindo ao usuário que insira a distância da viagem em milhas. A função inputé
usada para obter esse valor, que é convertida em um número de ponto flutuante e armazenado na variável
distancia_km.

2 - O código define o custo do combustível por milha. Nesse caso, ele assume que o veículo consome
0,1 litro de combustível por rodovia e que o preço do litro de combustível é R$5,00. O cálculo do
custo por mineração é realizado e armazenado em variável custo_por_km.

3 - O código calcula o custo total da viagem multiplicando a distância da viagem (em milhas) pelo
custo por milha. O resultado é armazenado na variável custo_total.

4 - Por fim, o código exibe o resultado, que é o custo total do combustível para a viagem em reais
(R$), formatado com duas casas decimais, usando a função round(custo_total, 2).

Este código é um exemplo prático de como usar variáveis, cálculos matemáticos e entrada/saída de
dados para calcular o custo de combustível de uma viagem com base na distância percorrida e no
consumo do veículo. Pode ser usado para ensinar conceitos de cálculos financeiros simples em Python.
'''
