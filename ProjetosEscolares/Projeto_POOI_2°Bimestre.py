'''
    Projeto do 2° Bimestre do segundo ano do Técnico em Informática.
    Programa que permite a digitação de vários CPF's para o usuário e verifica se são válidos ou não. Ao final da execução, mostra estatísticas dos CPF's digitados. 
'''

numVal = 0
numInval = 0
CPF_Testagem = 0
cpfsTestados = []
dicCPFs = {}
Teste1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
Teste2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]


# Procedimento para validar a escolha vai ou para
def _validacao_escolha():
    global escolha
    while True:
        if escolha.isnumeric():
            escolha = int(escolha)
            if (escolha >= 1) and (escolha <= 2):
                break
        escolhido = input('Escolha inválida. Digite novamente (1-Sim, 2- Não): ')


# Procedimento para ver se digito CPF está dentro dos parâmetros
def _validacao_num_cpf():
    global CPF_Testagem
    while True:
        if CPF_Testagem.isnumeric():
            CPF_Testagem = int(CPF_Testagem)
            if (CPF_Testagem >= 0) and (CPF_Testagem <= 9):
                break
        CPF_Testagem = input(f'Dígito inválido. Digite o {c + 1} dígito do CPF novamente: ')


# Função para saber se o CPF é válido
def _validacao_cpf(cpfteste, teste):
    soma = 0
    digitocpf = 0

    # Somar os produtos entre os primeiros números do CPF com o números de apoio
    for i in range(0, len(cpfteste)):
        soma += cpfteste[i] * teste[i]

    # Verificar resto entre soma e 11
    restoSoma = soma % 11

    # Descobrir o dígito
    if restoSoma < 2:
        digitocpf = 0
    else:
        digitocpf = 11 - restoSoma

    return digitocpf


# PROGRAMA PRINCIPAL
escolha = input('Quer começar a validação dos CPFs? (1-Sim, 2- Não): ')
if escolha == 1:

    _validacao_escolha()

    while escolha == 1:
        cpf = []
        cpfTeste1 = []
        cpfTeste2 = []
        digitoCpf1 = 0
        digitoCpf2 = 0

        # Digitar número CPF
        for c in range(0, 11):
            CPF_Testagem = input(f'Digite o {c + 1} número do CPF: ')
            _validacao_num_cpf()
            print(CPF_Testagem)
            cpf.append(CPF_Testagem)

        dicCPFs['CPF'] = cpf

        # Separar 9 primeiros digitos do CPF
        for c in range(0, 9):
            cpfTeste1.append(cpf[c])
            cpfTeste2.append(cpf[c])

        # Chamando função
        digitoCpf1 = _validacao_cpf(cpfTeste1, Teste1)

        # Conferindo se o número encontrado é igual ao digitado
        if cpf[9] == digitoCpf1:
            soma = 0
            cpfTeste2.append(cpf[9])

            # Chamando função
            digitoCpf2 = _validacao_cpf(cpfTeste2, Teste2)

            # Conferindo se o número encontrado é igual ao digitado
            if cpf[10] == digitoCpf2:
                dicCPFs['VALIDACAO'] = 'Válido'
                numVal += 1
            else:
                dicCPFs['VALIDACAO'] = 'Inálido'
                numInval += 1

        else:
            dicCPFs['VALIDACAO'] = 'Inálido'
            numInval += 1

        cpfsTestados.append(dicCPFs.copy())

        print(100 * '-')
        escolha = input('Quer continuar a validação dos CPFs? (1-Sim, 2- Não): ')
        _validacao_escolha()

    porcVal = (100 * numVal) / len(cpfsTestados)
    porcInval = (100 * numInval) / len(cpfsTestados)

    print(f'\n\nForam testados um total de {len(cpfsTestados)} CPFs')
    print(f'Dos CPFs testados, {numVal} foram válidos e {numInval} foram inválidos')
    print(f'Do total, {porcVal}% dos CPFs são válidos e {porcInval}% dos CPFs são inválidos')
else:
    print("Programa encerrado!")
