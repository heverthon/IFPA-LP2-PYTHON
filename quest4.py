''' 4) Escreva um programa que leia uma temperatura em Fahrenheit e a apresente convertida em graus
Celsius. A fórmula de conversão é C = (F – 32) * ( 5 / 9), na qual F é a temperatura em Fahrenheit e
C é a temperatura em Celcius. '''
f = float(input("Digite a temperatura em Fahrenheit: "))
c = (f - 32) * (5 / 9)
print("Sua temperatura em graus Fahrenheit é: " ,f, "Fº, e convertido para Celcius é: " ,c, "Cº")
