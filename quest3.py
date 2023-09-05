'''Escreva um programa em Python que leia uma temperatura em graus Celsius e apresente-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5,na qual F é a
temperatura em Fahrenheit e C é a temperatura em Celsius;'''

c = int(input("Digite o valor em graus Celsius: "))
f = (9 * c + 160) / 5
print("A temperatura em graus Celsius é: " ,c, "Cº, a temperatura em Fahrenheit é: " ,f, "Fº")
