''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No fim mostre os dez primeiros termos dessa
progreção.
                                            A formula de uma PA é:
                            * a[n] = a[1] + (n-1)r | r é a razão da PA, n o numero de termos '''

# Entrada de dados

a1 = int(input('Informe o primeiro termo de sua PA: '))
r = int(input('Informe a razão da sua PA: '))

# Laço da PA
print('=-' * 10, 'SUA PA COM r = {} e a[1] = {}'.format(r, a1), '-=' * 10)
for n in range(1, 11):
    a = a1 + (n - 1) * r
    print('{}\n'.format(a), end='')
