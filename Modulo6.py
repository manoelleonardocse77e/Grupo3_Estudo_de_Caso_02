import csv
import os

# Função para salvar os profissionais em um arquivo CSV
def salvar_profissionais(filename, profissionais):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(profissionais[0].keys())  # Escreve o cabeçalho com os nomes das colunas
        for profissional in profissionais:
            writer.writerow(profissional.values())  # Escreve os dados do profissional

# Função para atribuir um profissional a um plantão
def atribuir_profissional_a_plantao(profissionais, escala):
    id_profissional = int(input("Digite o ID do profissional: "))
    plantao = input("Digite o nome do plantão (exemplo: Plantao1): ")

    for profissional in profissionais:
        if profissional['ID'] == id_profissional:
            profissional['Plantao'] = plantao
            profissional['Horas_Trabalhadas'] += 12  # Atribuir 12 horas de trabalho

            # Atualizar a escala de trabalho com o nome do profissional
            escala[plantao].append(profissional['Nome'])

            salvar_profissionais('Lista_Profissionais.csv', profissionais)  # Salva os dados após a atribuição
            print(f"Profissional {profissional['Nome']} atribuído ao plantão {plantao} com sucesso!")
            return

    print("ID de profissional não encontrado!")

# Função para criar uma escala de trabalho
def criar_escala_de_trabalho(profissionais):
    plantoes = ['Plantao1', 'Plantao2', 'Plantao3']  # Defina os nomes dos plantões
    escala = {}

    for plantao in plantoes:
        escala[plantao] = []

    while True:
        print("\nMenu de Escala de Trabalho:")
        print("1. Atribuir Profissional a Plantão")
        print("2. Visualizar Escala de Trabalho")
        print("3. Trocar Profissional de Plantão")
        print("4. Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            atribuir_profissional_a_plantao(profissionais, escala)
        elif escolha == '2':
            print("Escala de Trabalho:")
            for plantao, profissionais_atribuidos in escala.items():
                print(f"{plantao}: {', '.join(profissionais_atribuidos)}")
        elif escolha == '3':
            trocar_profissional_de_plantao(profissionais, escala)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

# Função para trocar um profissional de plantão
def trocar_profissional_de_plantao(profissionais, escala):
    id_profissional = int(input("Digite o ID do profissional que deseja trocar de plantão: "))
    novo_plantao = input("Digite o nome do novo plantão (exemplo: Plantao2): ")

    for profissional in profissionais:
        if profissional['ID'] == id_profissional:
            plantao_anterior = profissional['Plantao']
            profissional['Plantao'] = novo_plantao

            if plantao_anterior != '':
                # Remover o profissional do plantão anterior na escala
                escala[plantao_anterior].remove(profissional['Nome'])
            escala[novo_plantao].append(profissional['Nome'])

            salvar_profissionais('Lista_Profissionais.csv', profissionais)  # Salva os dados após a troca
            print(f"Profissional {profissional['Nome']} transferido para o plantão {novo_plantao} com sucesso!")
            return

    print("ID de profissional não encontrado!")

# Função para cadastrar um novo profissional
def cadastrar_profissional(profissionais):
    nome = input("Digite o nome do profissional: ")
    cargo = input("Digite o cargo do profissional: ")
    experiencia = input("Digite a experiência do profissional: ")
    contato = input("Digite as informações de contato do profissional: ")

    # Gere um ID único para o novo profissional
    if not profissionais:
        novo_id = 1
    else:
        novo_id = int(profissionais[-1]['ID']) + 1

    profissional = {
        'ID': novo_id,
        'Nome': nome,
        'Cargo': cargo,
        'Experiencia': experiencia,
        'Contato': contato,
        'Plantao': '',
        'Horas_Trabalhadas': 0
    }

    profissionais.append(profissional)
    salvar_profissionais('Lista_Profissionais.csv', profissionais)  # Salva os dados após cada cadastro
    print(f"Profissional cadastrado com sucesso e salvo! ID: {novo_id}")

# Lista para armazenar os profissionais
profissionais = []

# Verificar se o arquivo Lista_Profissionais.csv existe
if os.path.exists('Lista_Profissionais.csv'):
    with open('Lista_Profissionais.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            profissionais.append(row)

while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Profissional")
    print("2. Escala de Trabalho")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        cadastrar_profissional(profissionais)
    elif escolha == '2':
        criar_escala_de_trabalho(profissionais)
    elif escolha == '3':
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
