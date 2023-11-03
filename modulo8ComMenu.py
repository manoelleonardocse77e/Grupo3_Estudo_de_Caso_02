# Nesse código dá pra acicionar as métricas de ocupação de leitos, e eficiência no uso de equipamentos
# Tem o código alternativo que consegue receber um relatório pronto, mas tem que implementar ele dentro desse.



import csv

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
