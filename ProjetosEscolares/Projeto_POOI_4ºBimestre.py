import mysql.connector
import pandas as pd


def planilha1():
    total = 0

    while True:
        try:
            registroProf = int(input('Digite o registro do professor para executar a 1° planinlha: '))

        except Exception as erro:
            print(error)
            print(f'Erro: {erro}')
            print(error)

        else:
            break

    # pega-se os dados necessários do BD
    comandoSQL.execute(
        f'select * from disciplinasxprofessores where codprofessor = {registroProf} and anoletivo = 2021;')
    dadosProfessor = comandoSQL.fetchall()

    # Cria a planilha
    planilha = pd.DataFrame(dadosProfessor)
    planilha['Total Carga Horária'] = 0

    for linha, dado in enumerate(planilha['cargahoraria']):
        total += int(dado)

    planilha['Total Carga Horária'] = total

    return planilha


def planilha2():
    dicionario = {}

    for linha, dado in enumerate(cursos):
        comandoSQL.execute(f'select distinct nomeprof from disciplinasxprofessores inner join '
                           f'professores on disciplinasxprofessores.codprofessor = professores.registro where curso ='
                           f' {dado["curso"]};')

        dadosProf = comandoSQL.fetchall()

        totalProf = 0
        lista = []

        for li, d in enumerate(dadosProf):
            lista.append(d['nomeprof'])
            totalProf = totalProf + 1

        lista.append(f'Total Professores no Curso: {totalProf}')
        dicionario[f'Curso{dado["curso"]}'] = lista

    planilha = pd.DataFrame.from_dict(dicionario, orient='index')
    planilha = planilha.transpose()
    return planilha


def planilha3():
    dicionario = {}

    for linha, dado in enumerate(cursos):
        tempoTotal = 0
        lista = []
        comandoSQL.execute(f'select nomedisc, cargahoraria from disciplinasxprofessores inner join disciplinas on '
                           f'disciplinasxprofessores.coddisciplina = disciplinas.codigodisc where '
                           f'curso = {dado["curso"]} and anoletivo = 2021;')
        dadosCurso = comandoSQL.fetchall()

        for li, d in enumerate(dadosCurso):
            lista.append(d['nomedisc'])
            tempoTotal = tempoTotal + d['cargahoraria']

        lista.append(f'Total Carga Horário do Curso: {tempoTotal}')
        dicionario[f'Curso{dado["curso"]}'] = lista

    planilha = pd.DataFrame.from_dict(dicionario, orient='index')
    planilha = planilha.transpose()
    return planilha


# ===============PROGRAMA PRINCIPAL===================
error = 50 * '-'

while True:
    try:
        # conectar BD
        conexaoSQL = mysql.connector.Connect(host='localhost', database='univap', user='root', password='')
        comandoSQL = conexaoSQL.cursor(dictionary=True)
        comandoSQL.execute('select distinct curso from disciplinasxprofessores where anoletivo = 2021;')
        cursos = comandoSQL.fetchall()

        pl1 = planilha1()
        pl2 = planilha2()
        pl3 = planilha3()

        comandoSQL.close()
        conexaoSQL.close()

        # Criar arquivo PDF
        arquivo = pd.ExcelWriter('2HID-POOI-Andrey Prado de Oliveira-Larissa de Oliveira Marangon Ramalho-Maria Eduarda dos Santos Pinto Ferreira.xlsx', engine='openpyxl')

        pl1.to_excel(arquivo, sheet_name='Tabela 1', index=False)
        pl2.to_excel(arquivo, sheet_name='Tabela 2', index=False)
        pl3.to_excel(arquivo, sheet_name='Tabela 3', index=False)
        
    except Exception as erro:
        print(error)
        print(f'Erro: {erro}')
        print(error)

    else:
        break

arquivo.save()
