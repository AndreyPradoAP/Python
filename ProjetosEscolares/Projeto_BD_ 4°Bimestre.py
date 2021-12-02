'''
    Projeto do 4° Bimestre do segundo ano do Técnico em Informática.
    Programa que simula um sistema de caixa eletrônico, onde é possível consultar saldo, fazer saque, fazer depósito e solicitar empréstimo. Após a finalização do programa pelo usuário, os dados são slavos dentro do banco de dados.
    Obs: O banco de dados utilizado foi o MongoDB.
         Video do programa funcionando: https://www.youtube.com/watch?v=ORIj6bTJSdA&t=5s
'''

import pymongo


def consultarSaldo():
    print('\n\n---------------------CONSULTA SALDO---------------------\n\n'
          f'Saldo = R${saldo}')


def fazerSaque(saldoFunc):
    print('\n\n---------------------FAZER SAQUE---------------------\n\n')

    try:
        saque = float(input('Digite o valor a ser sacado: '))

    except Exception as erro:
        print(50 * '-')
        print(f'Erro: {erro}')
        print(50 * '-')

    else:
        if saque > saldoFunc:
            print('Operação inválida, valor do saque maior que o saldo!')

        else:
            saldoFunc = saldoFunc - saque
            print('\nSaldo realizado com sucesso!')
            return saldoFunc


def fazerDeposito(saldoFunc):
    print('\n\n---------------------FAZER DEPOSITO---------------------\n\n')

    try:
        deposito = float(input('Digite o valor a ser depositado: '))

    except Exception as erro:
        print(50 * '-')
        print(f'Erro: {erro}')
        print(50 * '-')

    else:
        saldoFunc = saldoFunc + deposito
        print('\nDeposito realizado com sucesso!')
        return saldoFunc


def solicitarEmprestimo(saldoFunc):
    print('\n\n---------------------SOLICITAR EMPRESTIMO---------------------\n\n')

    try:
        emprestimo = float(input('Digite o valor para o emprestimo (Até 50% do valor total do saldo): '))

    except Exception as erro:
        print(50 * '-')
        print(f'Erro: {erro}')
        print(50 * '-')

    else:
        if emprestimo > saldo / 2:
            print('Operação inválida, valor do saque maior que 50% do saldo')
            return saldoFunc, 0, 0

        else:
            numParcelas = int(input('\nDigite a quantidade de parcelas para pagar o emprestimo: '))
            valorParcelas = (emprestimo / numParcelas) * 1.5
            saldoFunc = saldoFunc + emprestimo
            print('\nDeposito realizado com sucesso!')
            return saldoFunc, numParcelas, valorParcelas


# Programa Principal
saldo = 0.0
qtdParcelas = 0
valParcelas = 0

while True:
    print('\n\n-------------------------------MENU BANCO SANTOANDRE-------------------------------\n')
    print('0 - ENCERRAR PROGRAMA\n'
          '1 - CONSULTAR SALDO\n'
          '2 - FAZER SAQUE\n'
          '3 - FAZER DEPÓSITO\n'
          '4 - SOLICITAR EMPRÉSTIMO\n')

    try:
        escolha = int(input('Digite a sua escolha: '))

    except Exception as erro:
        print(50 * '-')
        print(f'Escolha inválida, erro: {erro}')
        print(50 * '-')

    else:
        if escolha == 0:
            dados = pymongo.MongoClient('mongodb://localhost:27017/').BancoSantoAndre.Clientes
            dados.insert_one({"Saldo": saldo, "Empréstimo": [
                {"Quantidade de parcelas": qtdParcelas, "Valor das Parcelas": valParcelas}]})
            break

        elif escolha == 1:
            consultarSaldo()

        elif escolha == 2:
            saldo = fazerSaque(saldo)

        elif escolha == 3:
            saldo = fazerDeposito(saldo)

        elif escolha == 4:
            saldo, qtdParcelas, valParcelas = solicitarEmprestimo(saldo)

        else:
            print(50 * '-')
            print('Escolha inexistente!')
            print(50 * '-')
