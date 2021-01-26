''' Escreva um programa que leia um numero inteiro qualquer e mostre na tela os primeiros elementos da sequencia
fibonacci '''

# Elementos a serem usados na sequencia Fibonacci
c = 0 # Contador para sequencia fibonacci
f1 = 1 # Primeiro elemento da sequencia fibonacci
fn = 0
f2 = 0
x = ''
# Numero te termos da Sequencia de Fibonacci

n = int(input('Informe qual o termo desejado para a sua sequencia Fibonacci: '))

while c < n+1:
    fn = f1 + f2 # Formula para a sequencia fibonacci
    if c > 0: # A partir do 2ndo loop entre nessa condição
        f2 = f1 # f[n-2] recebe f[n-1]
        f1 = fn # f[n-1] recebe f[n]

    x += str(fn) + ' ' # TRANSFORMA fn em string concatenando os valores e a cada valor concatena com 1 espaço
    print(x)
    c += 1


