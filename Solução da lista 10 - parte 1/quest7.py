#Questão 7
# Inicializa a soma das notas
soma_notas = 0

# Recebe as notas das 4 provas e acumula a soma
for i in range(1, 5):
    nota = float(input(f"Digite a nota da prova {i}: "))
    soma_notas += nota

# Calcula a média final
media_final = soma_notas / 4

# Exibe o resultado
print("A média final do aluno é:", round(media_final, 2))

'''
A explicação para os alunos seria a seguinte:

1 - O código começa inicializando a variável soma_notascom o valor zero.
Esta variável será usada para acompanhar a soma das notas das quatro provas.

2 - Em seguida, o código utiliza um loop forpara iterar através das quatro
provas. O loop vai de 1 a 4 (inclusive), e a variável irepresenta o número
da prova atual.

3 - Dentro do loop, o código solicita ao usuário que insira a nota da prova atual.
A nota é convertida em um número de ponto flutuante (float) e é adicionada à variável
soma_notas. Isso acumula a soma das notas à medida que as notas são inseridas.

4 - Após o loop ter acumulado a soma das notas das quatro provas, o código calcula
a média final dividindo a soma das notas por 4 e armazena o resultado na variável
media_final.

5 - Por fim, o código exibe o resultado, que é a média final do aluno, formatada
com duas casas decimais, usando a função round(media_final, 2).

Este código é um exemplo prático de como usar estruturas de repetição (loops),
entrada de dados, variáveis ​​e cálculos matemáticos para calcular a média final
de um aluno com base nas notas de quatro provas. Pode ser usado para ensinar
conceitos de iteração e cálculos de média em Python.
'''
