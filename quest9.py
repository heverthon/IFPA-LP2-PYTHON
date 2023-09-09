'''9) Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. (nota1= peso 6 e
nota2= peso 4)'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
peso1 = 6
peso2 = 4
media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print("A média ponderada das notas é: " ,media)
