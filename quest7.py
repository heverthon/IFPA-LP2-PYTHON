'''7) Escreva um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
que este sofreu um desconto de 10%.'''

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
nv_valor = preco * (1 - 0.10)
print("O Valor do produto com desconto é: " , nv_valor)
