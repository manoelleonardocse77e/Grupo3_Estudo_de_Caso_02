import csv

def registrar_equipamento():
    ref = int(input("Referência do Equipamento:\n(Número de Série)\n"))
    nome = input("Nome do Equipamento:\n")
    data = input("Data de Aquisição:\n")
    modelo = input("Modelo do Equipamento:\n")
    
    equipamento = {
        "Referência": ref,
        "Nome": nome,
        "Data de Aquisição": data,
        "Modelo": modelo
    }

    registrar_csv(equipamento)

def registrar_csv(equipamento):
    fieldnames = ["Referência", "Nome", "Data de Aquisição", "Modelo"]

    with open("registro_equipamento.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(equipamento)

def registrar_manutencao():
    equip = input("Equipamento Reparado:\n")
    data = input("Data da Manutenção:\n")
    manu = input("Manutenção Realizada:\n")
    interv = input("Intervenção Realizada:\n")

    manutencao = {
        "Equipamento": equip,
        "Data": data,
        "Manutenção": manu,
        "Intervenções": interv
    }

    salvar_manutencao(manutencao)

def salvar_manutencao(manutencao):
    fieldnames = ["Equipamento", "Data", "Manutenção", "Intervenções"]

    with open("historico_equipamento.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(manutencao)

menu = int(input("1 - Registrar Equipamento\n2 - Registrar Manutenção\n3 - Histórico de Manutenções\n4 - Programar Manutenção de Equipamento\n"))

if menu == 1:
    registrar_equipamento()

elif menu == 2:
    registrar_manutencao()

elif menu == 3:
    registro_equipamento = []
    Equipamento = input("Referência do Equipamento:\n")
    print("Equipamento\t\tData\t\tManutenção\t\tIntervenções")
    with open("historico_equipamento.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for linha in reader:
            ordem = {}
            for coluna in linha.keys():
                ordem[coluna] = linha[coluna]
            if Equipamento == ordem["Equipamento"]:
                registro_equipamento.append(ordem)
                print(f"{linha['Equipamento']}\t\t{linha['Data']}\t\t{linha['Manutenção']}\t\t{linha['Intervenções']}")