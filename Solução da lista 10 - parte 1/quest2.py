#Questão 2
# Recebe as dimensões da parede do usuário
largura_parede = float(input("Digite a largura da parede em metros: "))
altura_parede = float(input("Digite a altura da parede em metros: "))

# Define as dimensões de um tijolo em metros
largura_tijolo = 0.2
altura_tijolo = 0.1

# Calcula a quantidade de tijolos necessária para cobrir a parede
# Primeiro, calcula quantos tijolos cabem em um metro quadrado (tijolos por metro quadrado)
tijolos_por_metro_quadrado = (1 / largura_tijolo) * (1 / altura_tijolo)

# Em seguida, multiplica esse valor pelo total de metros quadrados da parede para obter a quantidade total de tijolos
quantidade_tijolos = largura_parede * altura_parede * tijolos_por_metro_quadrado

# Exibe a quantidade de tijolos necessários para cobrir a parede
print("Quantidade de tijolos necessários:", int(quantidade_tijolos))

'''

A explicação para os alunos seria a seguinte:

1 - O código começa pedindo que o usuário insira a largura e a altura da parede que deseja cobrir com tijolos. Essas
informações são obtidas por meio de duas chamadas à função inpute são convertidas em números de ponto flutuante (float)
e armazenadas nas variáveis largura_parede​​e altura_parede.

2 - O código define as dimensões de um tijolo com as variáveis largura_tijolo​​e altura_tijolo. Essas dimensões são usadas
para calcular quantos tijolos são necessários para cobrir um metro quadrado de parede.

3 - O código calcula a quantidade de tijolos necessários para cobrir a parede. Ele começa calculando quantos tijolos cabem
em um metro quadrado de parede, usando a fórmula (1 / largura_tijolo) * (1 / altura_tijolo). Em seguida, multiplique essa
quantidade pelo total de metros quadrados da parede, representado por largura_parede * altura_parede.

4 - Por fim, o código exibe a quantidade de tijolos necessários para cobrir a parede, arredondando o valor para o número
inteiro mais próximo. Isso é feito com a função int(quantidade_tijolos).

Este código é um exemplo prático de como usar variáveis, cálculos matemáticos e entrada/saída de dados para resolver
um problema com Python. Pode ser usado para ensinar conceitos de manipulação de dados numéricos e cálculos de engenharia
simples.

'''
