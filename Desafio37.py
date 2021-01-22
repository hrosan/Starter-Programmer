'''  Escreva um programa que leia um numero inteiro e peça para o usuario escolher qual será a base de conversão
 1 - binario
 2 - octal
 3 - hexadecimal '''

# IMPORTANDO BIBLIOTECAS


# ENTRADA DE DADOS

print('Informe um valor para conversão de base\n'
      '\033[;35m1 - BINARIO \n'
      '2 - OCTAL\n'
      '3 - HEXADECIMAL\033[m\n')

conv = int(input('Informe a base de conversão aqui: '))
x = int(input('Informe um valor a ser convertido: '))

# CONDICIONAIS

if conv == 1:
    y = bin(x)  # CONVERTE O ARGUMENTO PARA BINARIO
    print('O valor {} em BINARIO é: \033[;36m{}\033[m'.format(x, y))
elif conv == 2:
    y = oct(x)  # CONVERTE O ARGUMENTO PARA OCTAL
    print('O valor {} em OCTAL é: \033[;36m{}\033[m'.format(x, y))
elif conv == 3:
    y = hex(x)  # CONVERTE O ARGUMENTO PARA HEXADECIMAL
    print('O valor {} em HEXADECIMAL é: \033[;36m{}\033[m'.format(x, y))
