'''7) Escreva um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
que este sofreu um desconto de 10%.'''

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.1
novo_preco = preco - desconto

print("O novo valor com desconto é: " , novo_preco)
