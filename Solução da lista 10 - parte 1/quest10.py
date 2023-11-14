#Questão 10 
# Inicializa a soma das temperaturas
soma_temperaturas = 0

# Recebe as temperaturas de cada dia da semana e acumula a soma
for i in range(1, 8):
    temperatura = float(input(f"Digite a temperatura do dia {i}: "))
    soma_temperaturas += temperatura

# Calcula a média de temperaturas
media_temperaturas = soma_temperaturas / 7

# Exibe o resultado
print("A média das temperaturas da semana é:", round(media_temperaturas, 2), "°C")

'''
A explicação para seus alunos seria a seguinte:

1. O código começa inicializando a variável `soma_temperaturas` com o valor zero. Esta variável será usada para acompanhar a soma das temperaturas dos sete dias da semana.

2. O código utiliza um loop `for` para iterar através dos sete dias da semana. O loop vai de 1 a 7 (inclusive), e a variável `i` representa o número do dia atual.

3. Dentro do loop, o código solicita ao usuário que insira a temperatura do dia atual. A temperatura é convertida em um número de ponto flutuante (float) e é adicionada à variável `soma_temperaturas`. Isso acumula a soma das temperaturas à medida que são inseridas.

4. Após o loop ter acumulado a soma das temperaturas dos sete dias, o código calcula a média das temperaturas dividindo a soma pelo número de dias (7) e armazena o resultado na variável `media_temperaturas`.

5. Por fim, o código exibe o resultado, que é a média das temperaturas da semana, formatada com duas casas decimais, usando a função `round(media_temperaturas, 2)`, e a unidade de medida Celsius (°C).

Este código é um exemplo prático de como usar estruturas de repetição (loops), entrada de dados, variáveis e cálculos matemáticos para calcular a média de temperaturas ao longo de uma semana. Pode ser usado para ensinar conceitos de iteração e cálculos de média em Python.
'''
