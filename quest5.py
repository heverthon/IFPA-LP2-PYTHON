''' 5) Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um programa em Python
para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu
colocar no tanque '''

preco_gasolina = float(input("Digite o valor do preço do litro da Gasolina: "))

pago = float(input("Digite o valor a ser pago R$: "))
litros = pago / preco_gasolina
print("O valor do litro da gasolina é R$: " ,preco_gasolina, "Você pagou R$: " ,pago, "Você colocou: ",litros,"L")


