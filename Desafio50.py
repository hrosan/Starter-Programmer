'''  Faça um programa que leia seis numeros inteiros e mostre a soma daqueles que forem pares. Se for impar desconsidere '''

import random

s = 0  # inicializar uma variavel de soma em 0
p = 0  # iniciar uma varivel de contagem de numeros pares
im = 0  # Iniciar uma variavel de contagem de numeros impares

for n in range(1, 7):
    c = random.randint(1,31) # Gera um numero inteiro aleatorio entre 1 e 30
    even = c % 2 # Recebe o resto da divisão de c por 2
    if even == 0:  # SE O RESTO DO NUMERO FOR 0
        s = s + c  # FAÇA A SOMA
        p += 1  # CONTE +1 NUMERO PAR
    elif even != 0:  # SE NÃO FOR 0
        im += 1  # CONTE +1
if n == 6 and p >= 1:
    print('A soma dos valores pares é: {}, você escolheu {} numeros pares'.format(s, p))
if n == 6 and p==0:
    print('Você escreveu todos os valores impares')
