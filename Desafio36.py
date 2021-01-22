'''  Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor
 da casa, salario do comprador e em quantos anos ele vai apagar. Calcule o valor da prestação mensal sabendo que ela
 não poderá exceder 30% do valor do salario, senão o emprestimo será negado. '''


from math import ceil

# Entrada de informações

sal = float(input('Informe o seu salario: \033[;32mR$\033[m'))  # Salario
val = float(input('Informe o valor do imóvel: R$'))  # O valor do imovel
pre = float(input('Em quantos anos você pretende pagar o imovel: '))  # Qtde de tempo em anos para finalizar o pagamento

# ==================== Tratamento das informações ===========================

# Quantidade de meses que serão divididas as parcelas
mes = int(pre * 12)  # Transforme a qtde de anos em meses para faciltar o calculo
print('Você irá parcelar seu imóvel em \033[;32m{}\033[m meses \n'.format(mes))

# Valor das parcelas mensais

par = val / mes  # mostra o valor de cada parcela a ser paga
print('Você pagará parcelas de \033[;33mR${:.2f}\033[m \n'.format(par))

# Calculo da % do valor da parcela em relação ao salario

percentil = (par / sal) * 100  # Percentil da parcela em relação ao salario
#print('A parcela representa \033[;35m{:.2f}%\033[m'.format(percentil))

# ============================== CONDICIONAIS ================================
if percentil <= 30:
    print('O SEU CRÉDITO IMOBILIARIO FOI APROVADO, PARABÉNS\n')
else:
    mes = ceil((val/sal)*(10/3))
    print('SEU CRÉDITO SERÁ APROVADO COM NO MINIMO DE \033[;35m{}\033[m PARCELAS\n'.format(mes))
    print('Cada parcela terá um valor de \033[;35mR${:.2f}\033[m'.format(val/mes))