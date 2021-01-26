''' Crie uma programa que leia uma uma frase frase e diga se ela é um palindromo, desconsiderando os espaços '''


frase = input('Informe uma frase:').strip().upper()
word = frase.split() # Separa a frase em uma cadeia de strings
junto = ''.join(word) # Une as frases sem os espaços
inverso = '' # Inicializa uma string vazia

for c in range(len(junto)-1, -1, -1): # VAI COMEÇAR DA ULTIMA LETRA, ATÉ A PRIMEIRA
    inverso += junto[c]

if inverso == junto:
    print('A sua frase é um palindromo')
    print(inverso)
else:
    print('A sua frase não é um palindromo')
    print(inverso)