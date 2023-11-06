import csv

def agendar_visitantes():
    paciente = int(input("ID do Paciente:\n"))
    data = int(input("Data da Visita:\n"))
    hora = int(input("Hora da Visita:\n"))

    agenda = {
        "Paciente": paciente,
        "Data": data,
        "Hora": hora
    }

    salva_visita(agenda)

def salva_visita(agenda):
    fieldnames = ["Paciente", "Data", "Hora"]

    with open("agenda_visitantes.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(agenda)

def restringir_visitas():
    paciente = int(input("ID do Paciente:\n"))
    num_max = int(input("Máximo de Visitantes:\n"))
    dura_max = int(input("DUração Máxima da Visita:\n"))
    hora_ok = int(input("Horários Permitidos:\n"))

    restricoes = {
        "Paciente": paciente,
        "Máximo": num_max,
        "Duração": dura_max,
        "Horários": hora_ok
    }

    salva_restricoes(restricoes)

def salva_restricoes(restricoes):
    fieldnames = ["Paciente", "Máximo", "Duração", "Horários"]

    with open("restricoes.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(restricoes)

def registrar_visitantes():
    nome = input("Nome do Visitante:\n")
    cpf = int(input("CPF Visitante:\n"))
    relacao = input("Relação com Paciente:\n")

    visitantes = {
        "Nome": nome,
        "CPF": cpf,
        "Relação": relacao
    }

    salva_visitante(visitantes)

def salva_visitante(visitantes):
    fieldnames = ["Nome", "CPF", "Relação"]

    with open("visitantes.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(visitantes)

def cadastrar_fluxo():
    cpf = int(input("CPF do Visitante:\n"))
    entrada = int(input("Hora da Entrada:\n"))
    saida = int(input("Hora da Saída:\n"))

    horario = {
        "CPF": cpf,
        "Entrada": entrada,
        "Saida": saida
    }

    salva_fluxo(horario)

def salva_fluxo(horario):
    fieldnames = ["CPF", "Entrada", "Saida"]

    with open("entrada_e_saida.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(horario)

menu = int(input("1 - Agendamento de Visitantes\n2 - Restrições de Visita\n3 - Registro de Visitantes\n4 - Controle de acesso\n5 - Notificação de Visitas Agendadas\n6 - Integração Com Prontuário Eletrônico\n7 - Cancelamento e Reamendamento\n8 - Registro de Entradas e Saídas\n9 - Notificação de Visitas Pendentes\n"))
verifica_visitante = "visitantes.csv"
if menu == 1:
    agendar_visitantes()

elif menu == 2:
    restringir_visitas()

elif menu == 3:
    registrar_visitantes()

elif menu == 4:
    encontrado = False
    CPF_Visitante = input("CPF do Visitante\n")
    with open(verifica_visitante, "r") as file:
        reader = csv.reader(file)
    
        for linha in reader:
            for campo in linha:
                if campo == CPF_Visitante:
                    encontrado = True
                    break
            if encontrado:
                break
    
    if encontrado:
        print("Acesso Autorizado")
    else:
        print("Acesso Negado")

#elif menu == 5:
    #não sei como poderia entregar essa parte

#elif menu == 6:
    #integração com o módulo 5

elif menu == 7:
    data = input("Data do Agendamento Para Cancelar")
    agenda_visitantes = "agenda_visitantes.csv"
    encontrado = False

    manter = []
    with open(agenda_visitantes, "r") as file:
        reader = csv.reader(file)
        
        for linha in reader:
            if data in linha:
                encontrado = True
            else:
                manter.append(linha)

    if encontrado:
        with open(agenda_visitantes, "w", newline='') as file:
            writer = csv.writer(file)
            for linha in manter:
                writer.writerow(linha)
        print("Agendamento Cancelado")
    else:
        print("Agendamento Não Encontrado")
    
elif menu == 8:
    cadastrar_fluxo()

#elif menu == 9:
    #Mesma coisa do Elemento 5