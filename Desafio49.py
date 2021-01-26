'''  Refazer o exercicio da tabuada de um numero, agora usando o laço for '''

# Importando biblioteca
from random import randint

# Entrada de dados
x = randint(1, 20)

# Laço de repetição
print('-' * 10, 'Tabuada do {}'.format(x), '-' * 10)
for n in range(1, 11):
    c = x * n
    print(' ' * 10, '{} x {} = {}'.format(x, n, c))
