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
            codCurso = int(input('Digite o código do novo curso: '))
            codDisci = int(input('Digite o codigo da disciplina do novo curso: '))
            codProf = int(input('Digite o codigo do professor do novo curso: '))
            nomeCurso = int(input('Digite o nome do novo curso: '))
            cargaHoraria = int(input('Digite a carga horária do novo curso: '))
            anoLetivo = int(input('Digite o ano letivo do curso: '))
            comandosql.execute(
                f'insert into disciplinasxprofessores values({codCurso}, {codDisci}, {codProf}, {nomeCurso}, {cargaHoraria}, {anoLetivo})')
            conexao.commit()

        except mysql.connector.errors.IntegrityError:
            print(50 * '-')
            print(f'Erro: Erro de integridade!')
            print(50 * '-')

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro.args}')
            print(50 * '-')

        else:
            print('\nCadatro realizado com sucesso!')
            break


def alterarCurso():
    while True:
        flag = 0
        try:
            pk = int(input('Digite o código do curso à ser alterado: '))
            comandosql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso = {pk}')
            registrosTbl = comandosql.fetchall()

            if comandosql.rowcount > 0:
                for dados in registrosTbl:
                    esco = int(input('Digite o dado a ser alterado (1 - Código da Disciplina, 2 - Cógigo do Professor, 3 - Nome do Curso, 4 - Carga Horária, 5 - Ano Letivo): '))

                    if esco == 1:
                        novoDado = int(input('\nDigite o novo Código da Disciplina: '))

                        if input(
                                f'Deseja realmente mudar o código {dados[esco]} para {novoDado}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(
                                f'update disciplinasxprofessores set coddisciplina = {novoDado} where codigodisciplinanocurso = {pk};')
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
                        novoDado = int(input('\nDigite o novo Código do Professor: '))

                        if input(
                                f'Deseja realmente mudar o código {dados[esco]} para {novoDado}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(
                                f'update disciplinasxprofessores set codprofessor = {novoDado} where codigodisciplinanocurso = {pk};')
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
                        novoDado = int(input('\nDigite o novo nome do curso: '))
                        if input(f'Deseja realmente mudar {dados[esco]} para {novoDado}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(
                                f'update disciplinasxprofessores set curso = {novoDado} where codigodisciplinanocurso = {pk};')
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
                        novoDado = int(input('\nDigite a nova carga horária do curso: '))
                        if input(f'Deseja realmente mudar a carga de {dados[esco]} para {novoDado} horas? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update disciplinasxprofessores set cargahoraria = {novoDado} where codigodisciplinanocurso = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

                        else:
                            print(50 * '-')
                            print(f'Update Cancelado!')
                            print(50 * '-')
                            flag = 1

                    elif esco == 5:
                        novoDado = int(input('\nDigite o novo ano letivo do curso: '))
                        if input(f'Deseja realmente mudar o ano letivo de {dados[esco]} para {novoDado}? (S-sim ou n-não): ') == 'S':
                            comandosql.execute(f'update disciplinasxprofessores set anoletivo = {novoDado} where codigodisciplinanocurso = {pk};')
                            conexao.commit()
                            print('\nUpdate concluído com sucesso!')
                            flag = 1
                            break

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

        except mysql.connector.errors.IntegrityError:
            print(50 * '-')
            print(f'Erro: Erro de integridade!')
            print(50 * '-')

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')


def deletarRegistro():
    while True:
        try:
            pk = int(input('Digite o código do curso à ser deletado: '))

            comandosql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso = {pk}')
            registrosTbl = comandosql.fetchall()

            if comandosql.rowcount > 0:
                if input(f'Deseja realmente excluir o registro {registrosTbl}? (S-sim ou n-não): ') == 'S':
                    comandosql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso = {pk}')
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

        except Exception as erro:
            print(50 * '-')
            print(f'Erro: {erro}')
            print(50 * '-')


def vizualizar():
    while True:
        try:
            tbl = int(input('Qual tabela desejas vizualizar (1 - Tabela professores, 2 - Tabela Disciplinas, 3 - Tabela Cursos): '))

        except ValueError:
            print(50 * '-')
            print('Erro: Digite APENAS números!')
            print(50 * '-')

        else:
            if tbl == 1:
                comandosql.execute('select * from professores')
                dadosTbl = comandosql.fetchall()
                grid = PrettyTable(['N° Registro', 'Nome', 'Telefone', 'Idade', 'Salario'])

                if comandosql.rowcount > 0:
                    for dados in dadosTbl:
                        grid.add_row([dados[0], dados[1], dados[2], dados[3], dados[4]])
                    print(grid)
                    break

            elif tbl == 2:
                comandosql.execute('select * from disciplinas')
                dadosTbl = comandosql.fetchall()
                grid = PrettyTable(['N° Disciplina', 'Nome Disciplina'])

                if comandosql.rowcount > 0:
                    for dados in dadosTbl:
                        grid.add_row([dados[0], dados[1]])
                    print(grid)
                    break

            elif tbl == 3:
                comandosql.execute('select * from disciplinasxprofessores')
                dadosTbl = comandosql.fetchall()
                grid = PrettyTable(
                    ['Registro Curso', 'Registro Disciplina', 'Registro Professor', 'Nome Curso', 'Carga Horária',
                     'Ano Letivo'])

                if comandosql.rowcount > 0:
                    for dados in dadosTbl:
                        grid.add_row([dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]])
                    print(grid)
                    break


# PROGRAMA PRINCIPAL
while True:
    print('\n\n-------------------------------MENU-------------------------------\n')
    print('0 - SAIR DO PROGRAMA\n'
          '1 - CADASTRAR UM NOVO CURSO\n'
          '2 - ALTERAR UM CADASTRO DE CURSO\n'
          '3 - EXCLUIR UM CADASTRO DE CURSO\n'
          '4 - CONSULTAR A TABELAS')
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
            print('\n\n---------------------CADASTRAR CURSO---------------------\n')

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
            print('\n\n---------------------ALTERAR CADASTRO CURSO---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')

            else:
                alterarCurso()
                comandosql.close()
                conexao.close()

        elif escolha == 3:
            print('\n\n---------------------DELETAR REGISTRO CURSO---------------------\n')

            try:
                comandosql, conexao = conectarBD()

            except Exception as error:
                print(50 * '-')
                print(f'Erro ao tentar conectar com o servidor: {error}')
                print(50 * '-')
            else:
                deletarRegistro()

        elif escolha == 4:
            print('\n\n---------------------VIZUALIZAR REGISTROS---------------------\n')

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
