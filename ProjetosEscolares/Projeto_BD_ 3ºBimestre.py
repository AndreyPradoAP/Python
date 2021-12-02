'''
    Projeto do 3° Bimestre do segundo ano do Técnico em Informática.
    Programa que possibilita o cadastro de um cliente no banco de dados e verifica se este é autorizado a ter um cartão de crédito.
    Obs: O banco de dados utilizado foi o MySQL.
         Ao final da criação do cartão de crédito, é criado um QR code com os seus dados.
         Video do programa funcionando: https://www.youtube.com/watch?v=UqVuhQcw-aQ&t=9s
'''

import random
import mysql.connector
import pyqrcode
import datetime


def conectarBD():
    conexao = mysql.connector.connect(host='localhost', database='banco_santoandre', user='root', password='')
    if conexao.is_connected():
        print('Conexão com o Banco de Dados estabelicida!\n')
        comandosql = conexao.cursor()
        return comandosql, conexao


def cadastro():
    while True:
        try:
            registro = int(input('Digite o registro do novo cliente: '))
            nome = input('Digite o nome do novo cliente: ')
            telefone = input('Digite o telefone do novo cliente: ')
            email = input('Digite o e-mail do novo cliente: ')
            cpf = int(input('Digite o CPF do novo cliente (Apenas números): '))
            score = int(input('Digite o Serasa Score do novo cliente: '))
            salario = float(input('Digite o salário do novo cliente: '))
            ano = int(input('Digite o ano de nascimento do novo cliente: '))
        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro.args}')
            print(50 * '-')
        else:
            comandosql.execute(f'insert into tbl_clientes values({registro}, "{nome}", "{telefone}", "{email}", "{cpf}", {score}, {salario}, {ano});')
            conexao.commit()
            print('\nCadatro realizado com sucesso!')
            comandosql.close()
            conexao.close()
            break


def cartaoCredito():
    numeroCartao = ''
    digitosVerificadores = ''
    while True:
        try:
            pk = int(input('Digite o registro do cliente a ser adquirido o cartão de crédito: '))
            comandosql.execute(f'select * from tbl_clientes where registro_cliente = {pk}')
            registro = comandosql.fetchall()
        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')
        else:
            if comandosql.rowcount > 0:
                for dados in registro:
                    ano = datetime.date.today()
                    ano = int(ano.strftime('%Y'))
                    idade = ano - dados[7]
                    if idade >= 16:
                        if dados[5] >= 500:
                            print('\nCliente aprovado para receber cartão!')

                            limite = 1.6 * dados[6]

                            for c in range(0, 4):
                                for i in range(0, 4):
                                    num = random.randint(0, 9)
                                    numeroCartao += str(num)
                                if c < 3:
                                    numeroCartao += ' '

                            for c in range(0, 3):
                                num = random.randint(0, 9)
                                digitosVerificadores += str(num)

                            diaFechaFatura = random.randint(1, 30)

                            print('\n\nDADOS DO CARTÃO:\n'
                                  f'Número do cartão: {numeroCartao}\n'
                                  f'Dígitos verificadores: {digitosVerificadores}\n'
                                  f'Limite: R${limite}\n'
                                  f'Dia do fechamento da fatura: {diaFechaFatura}\n\n')

                            comandosql.execute(f'insert into tbl_cartaocredito values({pk}, "{numeroCartao}", "{digitosVerificadores}", {limite}, {diaFechaFatura});')
                            conexao.commit()

                            qr = pyqrcode.create(f'Número do cartão: {numeroCartao}\n'
                                                 f'Dígitos verificadores: {digitosVerificadores}\n'
                                                 f'Limite: R${limite}\n'
                                                 f'Dia do fechamento da fatura: {diaFechaFatura}\n')
                            qr.png('DadosCartão.png', scale=6)
                            qr.show()
                            break
                        else:
                            print(50 * '-')
                            print(f'Atenção: Cliente selecionado não possuí o Score mínimo de 500 pontos!')
                            print('Voltando ao menu...')
                            print(50 * '-')
                            break

                    else:
                        print(50 * '-')
                        print(f'Atenção: Cliente selecionado não possuí a idade mínima de 16 anos!')
                        print('Voltando ao menu...')
                        print(50 * '-')
                        break
                break
            else:
                print(50 * '-')
                print(f'Erro: Nenhum cliente registrado com esse número!')
                print(50 * '-')


while True:
    print('\n\n-------------------------------MENU BANCO SANTOANDRE-------------------------------\n')
    print('1 - CADASTRAR NOVO CLIENTE\n'
          '2 - ADQUIRIR CARTÃO DE CRÉDITO\n'
          '0 - SAIR DO PROGRAMA\n')

    try:
        escolha = int(input('Digite sua escolha: '))
    except ValueError:
        print(50 * '-')
        print(f'Erro: Digite apenas os números dados como alternativa')
        print(50 * '-')
    else:
        if escolha == 0:
            print('\nPrograma finalizado!')
            break

        elif escolha == 1:
            print('\n\n---------------------CADASTRAR CLIENTE---------------------\n')
            try:
                comandosql, conexao = conectarBD()
            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                cadastro()

        elif escolha == 2:
            print('\n\n---------------------ADQUIRIR CARTÃO DE CRÉDITO---------------------\n')
            try:
                comandosql, conexao = conectarBD()
            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                cartaoCredito()
