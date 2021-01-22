''' Escreve um programa que leia dois numeros inteiros e compare-os, mostrando na tela as seguintes msg
- O primeiro é maior
- O segundo é maior
- Os numeros são igual '''

# IMPORTANDO BIBLIOTECAS

from random import randint

# Entrada de dados

n1 = randint(1, 5)
n2 = randint(1, 5)

# CONDICIONAIS

if n1 > n2:
    print('1) {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('2) {} é maior que {}'.format(n2, n1))
else:
    print('Os numeros são iguais: {}'.format(n1))
