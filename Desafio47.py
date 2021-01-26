''' Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50 na tela '''

# Laço de repetição

for n in range(1, 51): # PARA N dentro do intervalo [1 , 50]
    c = n % 2 # C recebe o resto da divisão entre n e 2
    if c == 0: # Se C for igual a 0
        print('O numero {} é par'.format(n)) # Mostre o numero referente a N na tela com a frase
    else: # se não
        continue # Continue
