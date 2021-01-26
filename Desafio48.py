''' Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no
 intervalo de 1 à 500 '''

# Laço de repetição
s = 0
for n in range(1, 500,2):
    mult = n % 3
    if mult == 0:
        s += n
if n == 499:
    print('\n O valor da soma de todos os impares divisiveis por 3 no intervalo é: \033[;33m{}\033[m'.format(s))
