"""Pra mais detalhes, os arquivos que podem ser recebidos ficam melhores nesse formato:

Um exemplo do conteúdo de um arquivo de relatório em formato .txt:

Relatório de Performance da UTI

Métricas de Ocupação de Leitos:
- Leitos ocupados: 15
- Leitos disponíveis: 5

Eficiência no Uso de Equipamentos:
- Respiradores em uso: 20
- Monitores cardíacos em uso: 12

Dados de Atendimento aos Pacientes:
- Paciente 1 - Diagnóstico: COVID-19, Tratamento: Oxigenoterapia, Progresso Clínico: Estável
- Paciente 2 - Diagnóstico: Infarto, Tratamento: Monitoramento cardíaco, Progresso Clínico: Melhorando
_________________________________________________________________________________________________________

Outro exemplo só que com o conteúdo de um arquivo de relatório em formato .csv poderia ser estruturado:

Nome,Idade,Diagnóstico
Paciente 1,45,COVID-19
Paciente 2,60,Infarto
Paciente 3,55,Acidente Vascular Cerebral

"""

import csv

class Relatorios:
    def __init__(self):
        self.dados_relatorio_txt = []
        self.dados_relatorio_csv = []
        self.dados_ocupacao = []
        self.dados_eficiencia = []
        self.dados_atendimento = []

    def ler_relatorio_txt(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                self.dados_relatorio_txt.append(linha.strip())

    def ler_relatorio_csv(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                self.dados_relatorio_csv.append(linha)

    # Restante das funções permanece inalterado

