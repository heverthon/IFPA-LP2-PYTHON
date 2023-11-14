#Questão 8 
# Recebe a quantidade de produtos e o preço unitário do usuário
quantidade = int(input("Digite a quantidade de produtos: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

# Calcula o desconto com base na quantidade de produtos
if quantidade >= 30:
    desconto = 0.15
elif quantidade >= 20:
    desconto = 0.10
elif quantidade >= 10:
    desconto = 0.05
else:
    desconto = 0

# Calcula o preço final com desconto aplicado
preco_final = (quantidade * preco_unitario) * (1 - desconto)

# Exibe o resultado
print("Preço final com desconto: R$", round(preco_final, 2))

'''
A explicação para seus alunos seria a seguinte:

1 - O código começa solicitando ao usuário que insira a quantidade de produtos
e o preço unitário de um produto. As funções inputsão usadas para obter esses
valores, que são convertidos em números inteiros (quantidade) e números de ponto
flutuante (preço_unitário) e armazenados nas variáveis ​​correspondentes.

2 - O código calcula o desconto com base na quantidade de produtos adquiridos.
Se um valor igual ou superior a 30, é aplicado um desconto de 15%. Se um valor
igual ou superior a 20, é aplicado um desconto de 10%. Se um valor for igual ou
superior a 10, é aplicado um desconto de 5%. Caso contrário, nenhum desconto é
aplicado.

3 - Em seguida, o código calcula o preço final com o desconto aplicado. Isso é
multiplicar a quantidade de produtos pelo preço unitário, e em seguida, subtraindo
o valor do desconto, se aplicável.

4 - Por fim, o código exibe o resultado, que é o preço final com desconto em reais
(R$), formatado com duas casas decimais, usando a função round(preco_final, 2).

Este código é um exemplo prático de como usar estruturas condicionais (if-elif-else),
entrada de dados, variáveis ​​e cálculos matemáticos para calcular o preço final de
produtos com base na quantidade comprada e em descontos aplicados. Pode ser usado
para ensinar conceitos de condicionais e cálculos de preços em Python.
'''
