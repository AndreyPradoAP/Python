import mysql.connector
from prettytable import PrettyTable


def conectarBD():
    conexao = mysql.connector.connect(host='localhost', database='univap', user='root', password='')
    if conexao.is_connected():
        print('Conexão com o Banco de Dados estabelicida!\n')
        comandosql = conexao.cursor()
        return comandosql, conexao


def cadastrar():
    while True:
        try:
            registroProf = int(input('Digite o registro do novo professor: '))
            nomeProf = input('Digite o nome do novo professor: ')
            telefoneProf = input('Digite o telefone do novo professor: ')
            idadeProf = int(input('Digite a idade do novo professor: '))
            salarioProf = float(input('Digite o salário do novo professor: '))
            comandosql.execute(f'insert into professores values({registroProf}, "{nomeProf}", "{telefoneProf}", {idadeProf}, {salarioProf})')
            conexao.commit()
            print('\nCadatro realizado com sucesso!')
            break

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')


def alterarProf():
    while True:
        flag = 0
        try:
            pk = int(input('Digite o número do registro do professor a ser alterado: '))
            comandosql.execute(f'select * from professores where registro = {pk}')
            registrosTbl = comandosql.fetchall()

            if comandosql.rowcount > 0:
                for dados in registrosTbl:
                    esco = int(input('Digite o dado a ser alterado (1 - Nome, 2 - Telefone, 3 - Idade, 4 - Salário): '))

                    if esco == 1:
                        novoNome = input('\nDigite o novo nome do professor: ')

                        if input(f'Deseja realmente mudar o nome de {dados[esco]} para {novoNome}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update professores set nomeprof = "{novoNome}" where registro = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

                        else:
                            print(50 * '-')
                            print(f'Update Cancelado!')
                            print(50 * '-')
                            flag = 1

                    elif esco == 2:
                        novoTel = input('\nDigite o novo telefone do professor: ')

                        if input(f'Deseja realmente mudar o telefone de {dados[esco]} para {novoTel}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update professores set telefoneprof = "{novoTel}" where registro = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

                        else:
                            print(50 * '-')
                            print(f'Update Cancelado!')
                            print(50 * '-')
                            flag = 1

                    elif esco == 3:
                        novaIdade = int(input('\nDigite a nova idade do professor: '))
                        if input(f'Deseja realmente mudar a idade de {dados[esco]} para {novaIdade}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update professores set idadeprof = "{novaIdade}" where registro = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

                        else:
                            print(50 * '-')
                            print(f'Update Cancelado!')
                            print(50 * '-')
                            flag = 1

                    elif esco == 4:
                        novoSal = float(input('\nDigite o novo salário do professor: '))
                        if input(f'Deseja realmente mudar o salário de {dados[esco]} para {novoSal}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update professores set salarioprof = "{novoSal}" where registro = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

                        else:
                            print(50 * '-')
                            print(f'Update Cancelado!')
                            print(50 * '-')
                            flag = 1

                    else:
                        print(50 * '-')
                        print('Escolha inválida, digite novamente')
                        print(50 * '-')

                if flag == 1:
                    break
            else:
                print(50 * '-')
                print(f'Registro inexistente! Digite novamente')
                print(50 * '-')

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')


def deletarRegistro():
    while True:
        try:
            pk = int(input('Digite o registro à ser deletado: '))

            comandosql.execute(f'select * from professores where registro = {pk}')
            registrosTbl = comandosql.fetchall()

            if comandosql.rowcount > 0:
                if input(f'Deseja realmente excluir o registro {registrosTbl}? (S-sim ou n-não): ') == 'S':
                    comandosql.execute(f'delete from professores where registro = {pk}')
                    conexao.commit()
                    print('Delete executado com sucesso!')
                    break

                else:
                    print(50 * '-')
                    print(f'Delete Cancelado!')
                    print(50 * '-')
                    break
            else:
                print(50 * '-')
                print(f'Registro inexistente! Digite novamente')
                print(50 * '-')

        except mysql.connector.errors.IntegrityError:
            print(50 * '-')
            print(f'Erro: O professor referido possuí um cadastro na tabela de Cursos!')
            print(50 * '-')

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')


def vizualizar():
    comandosql.execute('select * from professores')
    dadosTbl = comandosql.fetchall()
    grid = PrettyTable(['N° Registro', 'Nome', 'Telefone', 'Idade', 'Salario'])

    if comandosql.rowcount > 0:
        for dados in dadosTbl:
            grid.add_row([dados[0], dados[1], dados[2], dados[3], dados[4]])
        print(grid)


# PROGRAMA PRINCIPAL
while True:
    print('\n\n-------------------------------MENU-------------------------------\n')
    print('0 - SAIR DO PROGRAMA\n'
          '1 - CADASTRAR UM NOVO PROFESSOR\n'
          '2 - ALTERAR UM CADASTRO DE PROFESSOR\n'
          '3 - EXCLUIR UM CADASTRO DE PROFESSOR\n'
          '4 - CONSULTAR A TABELA DOS PROFESSORES')
    try:
        escolha = int(input('Digite sua escolha: '))

    except Exception as error:
        print(50 * '-')
        print(f'Escolha inválida, erro: {error}')
        print(50 * '-')

    else:
        if escolha == 0:
            print('\nPrograma Finalizado!')
            break

        elif escolha == 1:
            print('\n\n---------------------CADASTRAR PROFESSOR---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                cadastrar()
                comandosql.close()
                conexao.close()

        elif escolha == 2:
            print('\n\n---------------------ALTERAR CADASTRO PROFESSOR---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')

            else:
                alterarProf()
                comandosql.close()
                conexao.close()

        elif escolha == 3:
            print('\n\n---------------------DELETAR REGISTRO PROFESSOR---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                deletarRegistro()

        elif escolha == 4:
            print('\n\n---------------------VIZUALIZAR REGISTRO PROFESSOR---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                vizualizar()
                comandosql.close()
                conexao.close()

        else:
            print(50 * '-')
            print('Escolha inexistente!')
            print(50 * '-')
