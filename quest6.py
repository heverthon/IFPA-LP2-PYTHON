''' 6) Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Escreva um programa
que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e
o salário final do funcionário.'''

salario = float(input("Digite o valor do seu salário fixo: "))
vendido = float(input("Digite quanto você vendeu: "))
comissao = vendido * 0.04
salario_final = salario + comissao
print("Sua comissão foi R$: " ,comissao, "e seu salário final foi R$: " ,salario_final)
