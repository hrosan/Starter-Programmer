''' Faça um programa que leia um numero inteiro e diga se ele é primo ou não.'''

x = int(input('Informe um numero: '))
tot = 0
for c in range(1, x+1):
    if x % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[35m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(x, tot))
if tot == 2:
    print('O numero {} é primo'.format(x))
else:
    print('O numero {} não é primo'.format(x))
