import csv
import time
import pandas as pd
import os
import sys

#Começo do Módulo 1
def Modulo1():
  leitos = {
    'UTI': {
        'total': 10,
        'ocupados': 0
    },
    'Ala A': {
        'total': 20,
        'ocupados': 0
    },
    'Ala B': {
        'total': 15,
        'ocupados': 0
    }
  }

  def atualizar_csv():
    with open('ocupacao_leitos.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Ala', 'Leitos Totais', 'Leitos Ocupados'])
        for ala, info in leitos.items():
            writer.writerow([ala, info['total'], info['ocupados']])


  def monitorar_leitos():
    while True:
        print("\nMonitoramento em Tempo Real:")
        for ala, info in leitos.items():
            print(f"{ala}: {info['ocupados']} leitos em uso")
            print(f"Leitos disponiveis: {info['total'] - info['ocupados']}")
            print("=-=" * 10)
        for ala, info in leitos.items():
            if info['ocupados'] >= info['total']:
                print(f"ALERTA: Capacidade máxima atingida em {ala}!")

        time.sleep(30)

  def priorizar_leitos(ala, gravidade):
    if leitos[ala]['ocupados'] < leitos[ala]['total']:
        print(f"Admitindo paciente na {ala} devido à gravidade: {gravidade}")
        leitos[ala]['ocupados'] += 1
        atualizar_csv()
    else:
        print(f"Todos os leitos na {ala} estão ocupados. Aguarde.")


  def alocar_paciente_auto():
    paciente_id = input("Digite o ID do paciente: ")
    gravidade = input("Digite a gravidade do caso (de 1 a 10): ")

    try:
        gravidade = int(gravidade)
        if gravidade < 1 or gravidade > 10:
            print("Gravidade fora da faixa válida. Deve estar entre 1 e 10.")
        else:
            if gravidade >= 8:
                priorizar_leitos('UTI', f"Gravidade {gravidade}")
            elif gravidade >= 5:
                priorizar_leitos('Ala A', f"Gravidade {gravidade}")
            else:
                priorizar_leitos('Ala B', f"Gravidade {gravidade}")
    except ValueError:
        print("Gravidade inválida. Deve ser um número de 1 a 10.")


  def notificar_disponibilidade():
    while True:
        for ala, info in leitos.items():
            if info['ocupados'] < info['total']:
                print(f"Notificação: Leito disponível em {ala}")
        time.sleep(60)


  def historico_ocupacao():
    with open('ocupacao_leitos.csv') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            print(f"{linha[0]}: {linha[2]} / {linha[1]} leitos ocupados")


  def gerar_relatorio():
    with open('ocupacao_leitos.csv') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            print(f"{linha[0]}: {linha[2]} / {linha[1]} leitos ocupados")


  def alerta_capacidade_maxima():
    while True:
        for ala, info in leitos.items():
            if info['ocupados'] >= info['total'] - 1:
                print(f"ALERTA: Capacidade máxima se aproximando em {ala}!")
        time.sleep(60)


  if __name__ == "__main__":
    atualizar_csv()

    priorizar_leitos('UTI', 'Crítico')
    priorizar_leitos('Ala A', 'Moderado')
    priorizar_leitos('Ala B', 'Leve')

    import threading

    monitoramento_thread = threading.Thread(target=monitorar_leitos)
    notificacao_thread = threading.Thread(target=notificar_disponibilidade)
    alerta_thread = threading.Thread(target=alerta_capacidade_maxima)

    monitoramento_thread.start()
    notificacao_thread.start()
    alerta_thread.start()

    while True:
        print("\nOpções:")
        print("1. Gerar Relatório de Ocupação")
        print("2. Admitir Paciente Automaticamente")
        print("3. Sair")
        escolha = input("Escolha a opção: ")
        if escolha == '1':
            gerar_relatorio()
        elif escolha == '2':
            alocar_paciente_auto()
        elif escolha == '3':
            main()
            break

    monitoramento_thread.join()
    notificacao_thread.join()
    alerta_thread.join()

#Fim do Módulo 1

#Começo do Módulo 2
def Modulo2():
    
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
  
  menu = int(input("1 - Registrar Equipamento\n2 - Registrar Manutenção\n3 - Histórico de Manutenções\n4 - Programar Manutenção de Equipamento\n5 - Voltar\n"))
  
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

#Fim do Módulo 2

#Começo do Módulo 3
def Modulo3():
    medicamentos = {}
    estoque_medicamentos = {}
    lotes_medicamentos = {}
    registro_administracao = []

    def criar_arquivo_csv():
        with open('medicamentos.csv', 'w', newline='') as arquivo:
            cabecalho = ['ID', 'Nome', 'Princípio Ativo', 'Dosagem', 'Forma de Administração']
            writer = csv.writer(arquivo)
            writer.writerow(cabecalho)

    def carregar_medicamentos():
        criar_arquivo_csv()
        with open('medicamentos.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicamento_id = int(row['ID'])
                medicamentos[medicamento_id] = {
                    'Nome': row['Nome'],
                    'Princípio Ativo': row['Princípio Ativo'],
                    'Dosagem': row['Dosagem'],
                    'Forma de Administração': row['Forma de Administração']
                }
                estoque_medicamentos[medicamento_id] = 0
                lotes_medicamentos[medicamento_id] = []

    def cadastrar_medicamento():
        nome = input("Nome do medicamento: ")
        principio_ativo = input("Princípio ativo: ")
        dosagem = input("Dosagem: ")
        forma_administracao = input("Forma de administração: ")

        medicamento_id = len(medicamentos) + 1
        medicamentos[medicamento_id] = {
            'Nome': nome,
            'Princípio Ativo': principio_ativo,
            'Dosagem': dosagem,
            'Forma de Administração': forma_administracao
        }

        estoque_medicamentos[medicamento_id] = 0

        with open('medicamentos.csv', mode='a', newline='') as file:
            fieldnames = ['ID', 'Nome', 'Princípio Ativo', 'Dosagem', 'Forma de Administração']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'ID': medicamento_id, 'Nome': nome, 'Princípio Ativo': principio_ativo, 'Dosagem': dosagem, 'Forma de Administração': forma_administracao})

        print(f"Medicamento {nome} cadastrado com sucesso!")

    def listar_medicamentos():
        for medicamento_id, info in medicamentos.items():
            print("=-=" * 10)
            print(f"ID: {medicamento_id}")
            print(f"Nome: {info['Nome']}")
            print(f"Princípio Ativo: {info['Princípio Ativo']}")
            print(f"Dosagem: {info['Dosagem']}")
            print(f"Forma de Administração: {info['Forma de Administração']}")
            print(f"Quantidade disponível: {estoque_medicamentos[medicamento_id]}")
            print("=-=" * 10)
            time.sleep(3)

    def controle_estoque():
        while True:
            print("=-=" * 13)
            print("Controle de Estoque")
            print("1. Adicionar Medicamento ao Estoque")
            print("2. Remover Medicamento do Estoque")
            print("3. Voltar ao Menu Principal")
            print("=-=" * 13)
            escolha = input("Opção: ")

            if escolha == "1":
                listar_medicamentos()
                medicamento_id = int(input("ID do medicamento para adicionar ao estoque: "))
                quantidade = int(input("Quantidade a adicionar ao estoque: "))
                estoque_medicamentos[medicamento_id] += quantidade
                print(f"{quantidade} unidades de {medicamentos[medicamento_id]['Nome']} adicionadas ao estoque.")
            elif escolha == "2":
                listar_medicamentos()
                medicamento_id = int(input("ID do medicamento para remover do estoque: "))
                quantidade = int(input("Quantidade a remover do estoque: "))
                if quantidade <= estoque_medicamentos[medicamento_id]:
                    estoque_medicamentos[medicamento_id] -= quantidade
                    print(f"{quantidade} unidades de {medicamentos[medicamento_id]['Nome']} removidas do estoque.")
                else:
                    print("Quantidade insuficiente em estoque.")
            elif escolha == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def alertas_estoque_baixo():
        print("=-=" * 13)
        print("Medicamentos com estoque baixo:")
        for medicamento_id, quantidade in estoque_medicamentos.items():
            if quantidade <= 15:
                print(f"Nome: {medicamentos[medicamento_id]['Nome']}")
                print(f"Quantidade disponível: {quantidade}")
                print("=-=" * 13)

    def rastreamento_lotes():
        while True:
            print("=-=" * 13)
            print("Rastreamento de Lotes")
            print("1. Adicionar Lote")
            print("2. Listar Lotes por Medicamento")
            print("3. Voltar ao Menu Principal")
            print("=-=" * 13)
            escolha = input("Opção: ")

            if escolha == "1":
                listar_medicamentos()
                medicamento_id = int(input("ID do medicamento para adicionar lote: "))
                lote = input("Número do lote: ")
                data_validade = input("Data de validade (DD/MM/AAAA): ")
                lotes_medicamentos[medicamento_id].append({'Lote': lote, 'Data de Validade': data_validade})
                print(f"Lote {lote} adicionado para {medicamentos[medicamento_id]['Nome']}.")
            elif escolha == "2":
                listar_medicamentos()
                medicamento_id = int(input("ID do medicamento para listar lotes: "))
                print("Lotes para", medicamentos[medicamento_id]['Nome'])
                for lote_info in lotes_medicamentos[medicamento_id]:
                    print(f"Lote: {lote_info['Lote']}, Data de Validade: {lote_info['Data de Validade']}")
                print("=-=" * 13)
            elif escolha == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def registrar_administracao():
        while True:
            listar_medicamentos()
            continuar = int(input("Deseja Continuar?\n[1] Sim\n[2] Não\n-> "))
            if continuar == 1:
                medicamento_id = int(input("ID do medicamento administrado: "))
                if medicamento_id not in medicamentos:
                    print("ID de medicamento inválido. Tente novamente.")
                    continue
                quantidade = int(input("Quantidade administrada: "))
                paciente = input("Nome do paciente: ")
                dosagem = input("Dosagem: ")
                responsavel = input("Responsável pela administração: ")
                registro_administracao.append({
                    'Medicamento': medicamentos[medicamento_id]['Nome'],
                    'Quantidade': quantidade,
                    'Paciente': paciente,
                    'Dosagem': dosagem,
                    'Responsável': responsavel,
                    'Data e Hora': time.strftime('%Y-%m-%d %H:%M:%S')
                })
                estoque_medicamentos[medicamento_id] -= quantidade
                print(f"Administração registrada para {medicamentos[medicamento_id]['Nome']}.")

            elif continuar == 2:
                break
            else:
                print("Opção Invalida!")
                continue

    def listar_registro_administracao():
        print("=-=" * 13)
        print("Registro de Administração de Medicamentos")
        for admin_info in registro_administracao:
            print(f"Medicamento: {admin_info['Medicamento']}")
            print(f"Quantidade: {admin_info['Quantidade']}")
            print(f"Paciente: {admin_info['Paciente']}")
            print(f"Dosagem: {admin_info['Dosagem']}")
            print(f"Responsável: {admin_info['Responsável']}")
            print(f"Data e Hora: {admin_info['Data e Hora']}")
            print("=-=" * 13)
        time.sleep(3)

    carregar_medicamentos()

    while True:
        print("=-=" * 13)
        print("Escolha uma opção:")
        print("1. Cadastrar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Controle de Estoque")
        print("4. Alertas de Estoque Baixo")
        print("5. Rastreamento de Lotes")
        print("6. Registrar Administração de Medicamentos")
        print("7. Listar Registro de Administração")
        print("8. Sair")
        print("=-=" * 13)
        escolha = input("Opção: ")

        if escolha == "1":
            cadastrar_medicamento()
        elif escolha == "2":
            listar_medicamentos()
        elif escolha == "3":
            controle_estoque()
        elif escolha == "4":
            alertas_estoque_baixo()
        elif escolha == "5":
            rastreamento_lotes()
        elif escolha == "6":
            registrar_administracao()
        elif escolha == "7":
            listar_registro_administracao()
        elif escolha == "8":
            main()
        else:
            print("Opção inválida. Tente novamente.")
          
#Fim do Módulo 3

#Começo do Módulo 4 e 7
def Modulo4_7():
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

#Fim do Módulo 4 e 7

#Começo do Módulo 5
def Modulo5():
  class ProntuarioEletronico:
    def __init__(self, cadastro_arquivo, diagnostico_arquivo, tratamento_arquivo, evolucao_arquivo, anexos_arquivo):
        self.cadastro_arquivo = self.verificar_arquivo(cadastro_arquivo)
        self.diagnostico_arquivo = self.verificar_arquivo(diagnostico_arquivo)
        self.tratamento_arquivo = self.verificar_arquivo(tratamento_arquivo)
        self.evolucao_arquivo = self.verificar_arquivo(evolucao_arquivo)
        self.anexos_arquivo = self.verificar_arquivo(anexos_arquivo)

    def verificar_arquivo(self, arquivo):
        if not os.path.exists(arquivo):
            df = pd.DataFrame({'Nome': [], 'Idade': [], 'Sexo': [], 'Historico': [], 'Contato_de_Emergencia': []})
            df.to_csv(arquivo, index=False)
        return arquivo

    def cadastrar_paciente(self, nome, idade, sexo, historico, contato_emergencia):
        df = pd.read_csv(self.cadastro_arquivo)
        df = df._append({'Nome': nome, 'Idade': idade, 'Sexo': sexo, 'Historico': historico, 'Contato_de_Emergencia': contato_emergencia}, ignore_index=True)
        df.to_csv(self.cadastro_arquivo, index=False)
        print("Paciente cadastrado com sucesso.")

    def registrar_diagnostico(self, nome_paciente, data_diagnostico, descricao, recomendacoes):
        df = pd.read_csv(self.diagnostico_arquivo)
        df = df._append({'Nome_Paciente': nome_paciente, 'Data_Diagnostico': data_diagnostico, 'Descricao': descricao, 'Recomendacoes': recomendacoes}, ignore_index=True)
        df.to_csv(self.diagnostico_arquivo, index=False)
        print("Diagnóstico registrado com sucesso.")

    def acompanhar_tratamento(self, nome_paciente, medicamentos, procedimentos, terapias):
        df = pd.read_csv(self.tratamento_arquivo)
        df = df._append({'Nome_Paciente': nome_paciente, 'Medicamentos': medicamentos, 'Procedimentos': procedimentos, 'Terapias': terapias}, ignore_index=True)
        df.to_csv(self.tratamento_arquivo, index=False)
        print("Tratamento acompanhado com sucesso.")

    def documentar_evolucao(self, nome_paciente, data, mudancas, resultados_exames, observacoes):
        df = pd.read_csv(self.evolucao_arquivo)
        df = df._append({'Nome_Paciente': nome_paciente, 'Data': data, 'Mudancas': mudancas, 'Resultados_Exames': resultados_exames, 'Observacoes': observacoes}, ignore_index=True)
        df.to_csv(self.evolucao_arquivo, index=False)
        print("Evolução documentada com sucesso.")

    def anexar_documento(self, nome_paciente, tipo_documento):
        df = pd.read_csv(self.anexos_arquivo)
        df = df._append({'Nome_Paciente': nome_paciente, 'Tipo_Documento': tipo_documento}, ignore_index=True)
        df.to_csv(self.anexos_arquivo, index=False)
        print("Documento anexado com sucesso.")

  if __name__ == "__main__":
    for arquivo in ['cadastropacientes.csv', 'registrosdiagnosticos.csv', 'acompanhartratamentos.csv', 'evolucaoclinica.csv', 'anexosdocumentos.csv']:
        with open(arquivo, 'w') as f:
            f.write('Exemplo,Exemplo,Exemplo,Exemplo,Exemplo\n')

    prontuario = ProntuarioEletronico('cadastropacientes.csv', 'registrosdiagnosticos.csv', 'acompanhartratamentos.csv', 'evolucaoclinica.csv', 'anexosdocumentos.csv')

    while True:
        print("\n---- MENU ----")
        print("1. Cadastrar paciente")
        print("2. Registrar diagnóstico")
        print("3. Acompanhar tratamento")
        print("4. Documentar evolução")
        print("5. Anexar documento")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do paciente: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            historico = input("Histórico médico: ")
            contato_emergencia = input("Contato de emergência: ")
            prontuario.cadastrar_paciente(nome, idade, sexo, historico, contato_emergencia)

        elif escolha == '2':
            nome_paciente = input("Nome do paciente: ")
            data_diagnostico = input("Data do diagnóstico (YYYY-MM-DD): ")
            descricao = input("Descrição do diagnóstico: ")
            recomendacoes = input("Recomendações: ")
            prontuario.registrar_diagnostico(nome_paciente, data_diagnostico, descricao, recomendacoes)

        elif escolha == '3':
            nome_paciente = input("Nome do paciente: ")
            medicamentos = input("Medicamentos: ")
            procedimentos = input("Procedimentos: ")
            terapias = input("Terapias: ")
            prontuario.acompanhar_tratamento(nome_paciente, medicamentos, procedimentos, terapias)

        elif escolha == '4':
            nome_paciente = input("Nome do paciente: ")
            data = input("Data (YYYY-MM-DD): ")
            mudancas = input("Mudanças no estado de saúde: ")
            resultados_exames = input("Resultados de exames: ")
            observacoes = input("Observações: ")
            prontuario.documentar_evolucao(nome_paciente, data, mudancas, resultados_exames, observacoes)

        elif escolha == '5':
            nome_paciente = input("Nome do paciente: ")
            tipo_documento = input("Tipo de documento: ")
            prontuario.anexar_documento(nome_paciente, tipo_documento)

        elif escolha == '6':
            print("Voltando para o menu principal...")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

#Fim do Módulo 5

#Começo do Módulo 6
def Modulo6():
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

#Fim do Módulo 6

#Começo do Módulo 8
def Modulo8():
  class Relatorios:
    def __init__(self):
        self.dados_ocupacao = []
        self.dados_eficiencia = []
        self.dados_atendimento = []

    def gerar_relatorio_txt(self, dados, nome_arquivo):
        with open(nome_arquivo + '.txt', 'w') as arquivo_txt:
            for linha in dados:
                arquivo_txt.write(str(linha) + '\n')
        print(f"Relatório em formato .txt gerado com sucesso: {nome_arquivo}.txt")

    def gerar_relatorio_csv(self, dados, nome_arquivo, cabecalho):
        with open(nome_arquivo + '.csv', 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(cabecalho)
            escritor_csv.writerows(dados)
        print(f"Relatório em formato .csv gerado com sucesso: {nome_arquivo}.csv")

    def calcular_ocupacao_leitos(self):
        if not self.dados_ocupacao:
            print("Não há dados de ocupação de leitos.")
            return
        ocupacao = sum(self.dados_ocupacao) / len(self.dados_ocupacao)
        return ocupacao

    def avaliar_eficiencia_equipamentos(self):
        if not self.dados_eficiencia:
            print("Não há dados de eficiência de equipamentos.")
            return
        eficiencia = sum(self.dados_eficiencia) / len(self.dados_eficiencia)
        return eficiencia

    def coletar_dados_atendimento(self, diagnostico, tratamento, progresso_clinico):
        self.dados_atendimento.append({'diagnostico': diagnostico, 'tratamento': tratamento, 'progresso_clinico': progresso_clinico})


  # Função para exibir o menu
  def exibir_menu():
    print("\n1. Gerar relatório em formato .txt")
    print("2. Gerar relatório em formato .csv")
    print("3. Adicionar dados de ocupação de leitos")
    print("4. Adicionar dados de eficiência de equipamentos")
    print("5. Adicionar dados sobre o atendimento aos pacientes")
    print("6. Calcular métricas de ocupação de leitos")
    print("7. Avaliar eficiência no uso de equipamentos")
    print("8. Sair")


  relatorios = Relatorios()

  while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        dados_txt = ['Dados sobre a performance da UTI e do hospital', 'Métricas de ocupação de leitos', 'Eficiência no uso de equipamentos', 'Dados sobre atendimento aos pacientes']
        nome_arquivo = input("Digite o nome do arquivo .txt: ")
        relatorios.gerar_relatorio_txt(dados_txt, nome_arquivo)

    elif escolha == '2':
        cabecalho_csv = ['Nome', 'Idade', 'Diagnóstico']
        dados_csv = [['Paciente 1', 45, 'COVID-19'], ['Paciente 2', 60, 'Infarto']]
        nome_arquivo = input("Digite o nome do arquivo .csv: ")
        relatorios.gerar_relatorio_csv(dados_csv, nome_arquivo, cabecalho_csv)

    elif escolha == '3':
        dado_ocupacao = float(input("Digite a ocupação de leitos: "))
        relatorios.dados_ocupacao.append(dado_ocupacao)

    elif escolha == '4':
        dado_eficiencia = float(input("Digite a eficiência do equipamento: "))
        relatorios.dados_eficiencia.append(dado_eficiencia)

    elif escolha == '5':
        diagnostico = input("Digite o diagnóstico: ")
        tratamento = input("Digite o tratamento: ")
        progresso_clinico = input("Digite o progresso clínico: ")
        relatorios.coletar_dados_atendimento(diagnostico, tratamento, progresso_clinico)

    elif escolha == '6':
        ocupacao_leitos = relatorios.calcular_ocupacao_leitos()
        if ocupacao_leitos is not None:
            print(f'Métricas de ocupação de leitos: {ocupacao_leitos}%')

    elif escolha == '7':
        eficiencia_equipamentos = relatorios.avaliar_eficiencia_equipamentos()
        if eficiencia_equipamentos is not None:
            print(f'Eficiência no uso de equipamentos: {eficiencia_equipamentos}%')

    elif escolha == '8':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#Fim do Módulo 8

#Começo do Menu 2
def main2():
  print('Oque deseja: \n 1 - Localizar \n 2 - Excluir \n 3 - Voltar \n')

  opcao = int(input('Digite a opção: '))
  print('\n')
  
  match opcao:
    case 1:
      Localizar_arquivos()
    case 2:
      main3()
    case 3:
      main()
    case _:
      print('Opção inválida \n')
      main2()
#Fim do Menu 2

#Menu 3
def main3():
  excluir = int(input('Qual arquivo deseja excluir:\n1 - Ocupação de leitos\n 2 - Historico de equipamento\n 3 - Medicamentos\n 4 - Visitantes\n 5 - Lista de Profissionais\n '))

  match excluir:
    case 1:
      head = ['Ala','Leitos Totais','Leitos Ocupados']
      apagar_informacoes_csv('ocupacao_leitos.csv', head)
    case 2:
      head = []
      apagar_informacoes_csv('historico_equipamento.csv', head)
    case 3:
      head = ['ID','Nome','Princípio Ativo','Dosagem','Forma de Administração']
      apagar_informacoes_csv('medicamentos.csv',head)
    case 4:
      head = []
      apagar_informacoes_csv('visitantes.csv', head)
    case 5:
      head = ["ID", "Nome", "Cargo", "Experiencia", "Contato", "Plantao", "Horas_Trabalhadas"]
      apagar_informacoes_csv('Lista_Profissionais.csv', head)
    case _:
      print('Selecione uma opção valida!')

#Fim Menu 3

#Funções de Localização e Exclusão de arquivos
def Localizar_arquivos():
  
  localizar = int(input('Digite o número do arquivo que deseja localizar:\n 1 - Ocupação de leitos\n 2 - Historico de equipamento\n 3 - Medicamentos\n 4 - Visitantes\n 5 - Lista de Profissionais\n '))

  match localizar:
    case 1:
      with open('ocupacao_leitos.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
    case 2:
      with open('historico_equipamento.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
    case 3:
      with open('medicamentos.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
    case 4:
      with open('visitantes.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)
    case 5:
      with open('Lista_Profissionais.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            print(linha)


def apagar_informacoes_csv(filename, head):
  if not os.path.exists(filename):
    print(f"O arquivo '{filename}' não existe.")
    return

  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    header = [head]  # Defina o cabeçalho aqui
    writer.writerow(header)

  print(f"As informações do arquivo '{filename}' foram apagadas, mantendo apenas o cabeçalho.")

#Fim das Funções de Localização e Exclusão de arquivos

#Começo menu de escolhas
def main():
  while True:
    # Menu de escolha de módulos
    print('==-' * 13)
    print('\n')
    print('Tipos de módulos disponiveis para operação: \n 1 - Módulo de Gestão de Leitos \n 2 - Módulo de Controle de Equipamentos \n 3 - Módulo de Adiministração de Medicamentos \n 4 - Módulo de Agendamento e Controle de Visitas \n 5 - Módulo de Protuário Eletrônico \n 6 - Módulo de Gestão de equipes \n 7 - Módulo de Cadastro de Pacientes \n 8 - Módulo de Relatórios e Análises \n 9 - Localização e Exclusão de arquivos \n 0 - Sair do programa \n')

    escolha = int(input('Digite o número de um módulo que deseja operar: '))

    print('\n')

    match escolha:
      case 1:
        Modulo1()
        break
      case 2:
        Modulo2()
      case 3:
        Modulo3()
      case 4:
        Modulo4_7()
      case 5:
        Modulo5()
      case 6:
        Modulo6()
      case 7:
        Modulo4_7()
      case 8:
        Modulo8()
      case 9:
        main2()
      case 0:
        print('Saindo do programa...')
        break
      case _:
        print("Módulo inválido. Tente novamente.")

if __name__ == '__main__':
  main()

#Fim menu de escolhas
