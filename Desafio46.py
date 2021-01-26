'''  Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio. Indo do 10
 até o 0 com uma pausa de 1 seg. entre elas '''

# Importando a biblioteca
from time import sleep

for n in range(10, 0, -1):
    print(n)
    sleep(1)
    c = n
    if c == 1:
        print('Feliz Ano Novo!!!!!')
    else:
        continue
