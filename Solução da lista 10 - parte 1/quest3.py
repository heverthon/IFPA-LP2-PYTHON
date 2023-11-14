#Questão 3
# Recebe o número de produtos do usuário
n_produtos = int(input("Digite o número de produtos: "))

# Inicializa a variável 'total' para armazenar o valor total a ser pago
total = 0

# Calcula o total a ser pago
# Utiliza um loop 'for' para iterar através dos produtos
for i in range(n_produtos):
    # Solicita ao usuário que insira o preço do produto atual
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    
    # Adiciona o preço do produto ao total
    total += preco

# Exibe o resultado
print("Total a ser pago: R$", round(total, 2))

'''
A explicação para os alunos seria a seguinte:

1 - O código começa solicitando que o usuário insira o número de produtos que deseja calcular o total a ser pago.
A função inputé usada para obter esse valor, que é convertido em um número inteiro (int) e armazenado na variável n_produtos.

2 - A variável totalé inicializada com o valor zero. Essa variável será usada para acompanhar o valor total a ser pago pelos produtos.

3 - O código utiliza um loop forpara iterar através dos produtos. O loop vai de 0 até n_produtos - 1, e a variável
irepresenta o índice do produto atual.

4 - Dentro do loop, o código solicita ao usuário que insira o preço do produto atual. O preço é convertido em um número de
ponto flutuante e armazenado na variável preco.

5 - O preço do produto é adicionado ao valor total na variável total.

6 - Após o loop ter percorrido todos os produtos, o código exibe o resultado, que é o valor total a ser pago, formatado em reais
(R$) com duas casas decimais, usando a função round(total, 2).

Este código é um exemplo prático de como usar estruturas de reprodução (loops), entrada de dados, variáveis ​​e cálculos matemáticos
para calcular o total a ser pago por uma série de produtos. Pode ser usado para ensinar conceitos de iteração e acumulação de valores em Python.
'''
