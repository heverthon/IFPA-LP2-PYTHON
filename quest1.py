Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> funcionario = int(input("Digite seu CPF *Somente números: "))
Digite seu CPF *Somente números: 04256560203
>>> horas_trabalhadas = int(input("Digite suas horas trabalhadas: "))
Digite suas horas trabalhadas: 8
>>> recebe_por_hora = float(input("Digite o Valor que você recebe por hora: "))
Digite o Valor que você recebe por hora: 15,50
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    recebe_por_hora = float(input("Digite o Valor que você recebe por hora: "))
ValueError: could not convert string to float: '15,50'
>>> 
>>> recebe_por_hora = float(input("Digite  o Valor que você recebe por hora: "))
Digite  o Valor que você recebe por hora: 15.50
>>> salario_dia = horas_trabalhadas * recebe_por_hora
>>> salario_mes = salario_dia * 30
>>> print("O você recebe um valor mensal de: " ,salario_mes)
O você recebe um valor mensal de:  3720.0
