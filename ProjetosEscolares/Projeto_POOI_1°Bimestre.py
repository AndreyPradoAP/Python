'''
    Projeto do 1° Bimestre do segundo ano do Técnico em Informática.
    Programa que, através das escolhas de refeição do usuário, calcula a quantidade de calorias consumidas por ele, o prato consumido com maior quantidade de calorias,
    a porcentagem que equivale as calorias do prato principal em relação à quantidade de calorias consumidas na refeição e se op total de calorias consumidas estão na
    quantidade ideal para um dia.
    Obs: As calorias dos pratos são estabelecidas pelo programador;
         A quantidade de calorias ideal para ser consumidas em 1 dia é 2000kcal.
    
'''

# Função para validar digitação da escolha do alimento
def __escolha(escolhido, pergunta):
    while True:
        if escolhido.isnumeric():
            escolhido = int(escolhido)
            if (escolhido >= 1) and (escolhido <= 4):
                return escolhido
                break
        escolhido = input(pergunta)


# Função para validar digitação da quantidade do alimento
def ____quantidade(qtd, pergunta):
    while True:
        if qtd.isnumeric():
            qtd = int(qtd)
            if qtd > 0:
                return qtd
                break
        qtd = input(pergunta)


# Programa Principal
prato = input('Digite o prato escolhido (1 - Vegetariano, 2 - Peixe, 3 - Frango, 4 - Carne): \n')
prato = int(__escolha(prato, 'Escolha inválida! Digite o prato escolhido novamente (1 - Vegetariano, 2 - Peixe, 3 - Frango, 4 - Carne)\n'))
qtd_prato = input('Digite a quantidades de pratos consumidos\n')
qtd_prato = int(____quantidade(qtd_prato, 'Quantidade inválida! Digite a quantidades de pratos consumidos\n'))

sobremesa = input('\nDigite a sobremesa escolhida (1 - Abacaxi, 2 - Sorvete Diet, 3 - Mouse Diet, 4 - Mouse Chocolate)\n')
sobremesa = int(__escolha(sobremesa, 'Escolha inválida! Digite a sobremesa escolhida novamente (1 - Abacaxi, 2 - Sorvete Diet, 3 - Mouse Diet, 4 - Mouse Chocolate)\n'))
qtd_sobremesa = input('Digite a quantidades de sobremesas consumidas\n')
qtd_sobremesa = int(____quantidade(qtd_sobremesa, 'Quantidade inválida! Digite a quantidades de sobremesas consumidas\n'))

bebida = input('\nDigite a bebida escolhida (1 - Chá, 2 - Suco de Laranja, 3 - Suco de Melão, 4 - Refrigerante Diet)\n')
bebida = int(__escolha(bebida, 'Escolha inválida! Digite a bebida escolhida novamente (1 - Chá, 2 - Suco de Laranja, 3 - Suco de Melão, 4 - Refrigerante Diet)\n'))
qtd_bebida = input('Digite a quantidades de bebidas consumidas\n')
qtd_bebida = int(____quantidade(qtd_bebida, 'Quantidade inválida! Digite a quantidades de bebidas consumidas\n'))

cal_prato, cal_sobremesa, cal_bebida = 0, 0, 0
if prato == 1:
    cal_prato = 180
elif prato == 2:
    cal_prato = 230
elif prato == 3:
    cal_prato = 250
elif prato == 4:
    cal_prato = 350

if sobremesa == 1:
    cal_sobremesa = 75
elif sobremesa == 2:
    cal_sobremesa = 110
elif sobremesa == 3:
    cal_sobremesa = 170
elif sobremesa == 4:
    cal_sobremesa = 200

if bebida == 1:
    cal_bebida = 20
elif bebida == 2:
    cal_bebida = 70
elif bebida == 3:
    cal_bebida = 100
elif bebida == 4:
    cal_bebida = 65

total_cal_prato = cal_prato * qtd_prato
total_cal_sobremesa = cal_sobremesa * qtd_sobremesa
total_cal_bebida = cal_bebida * qtd_bebida

total_cal = total_cal_prato + total_cal_bebida + total_cal_sobremesa

maior_cal = total_cal_prato

if maior_cal < total_cal_sobremesa:
    maior_cal = total_cal_sobremesa
elif maior_cal < total_cal_bebida:
    maior_cal = total_cal_bebida

if maior_cal == total_cal_prato:
    maior_cal = 'o prato'
elif maior_cal == total_cal_sobremesa:
    maior_cal = 'a sobremesa'
elif maior_cal == total_cal_bebida:
    maior_cal = 'a bebida'

porcento_prato = 100 * total_cal_prato / total_cal

print('_' * 100)
print(f'\nA maior caloria consumida no dia foi {maior_cal};')
print(f'O total de calorias consumidas foram {total_cal} calorias;')
print(f'As calorias consumidas no(s) prato(s) são {porcento_prato:.2f}% do total de calorias consumidas;')

if (total_cal >= 0) and (total_cal < 1200):
    print(f'Cuidado! Calorias consumidas abaixo do ideal.')
elif (total_cal >= 1200) and (total_cal <= 1500):
    print(f'Calorias consumidas dentro do ideal.')
elif total_cal > 1500:
    print(f'Essa quantidade de calorias é prejudicial à saúde!')
