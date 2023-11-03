# Nesse código, ele cria uns nomes com "exemplos" dentro dos arquivos, mas não acrescenta nada, simplesmente faz funcionar !

import pandas as pd
import os

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
        df = df.append({'Nome': nome, 'Idade': idade, 'Sexo': sexo, 'Historico': historico, 'Contato_de_Emergencia': contato_emergencia}, ignore_index=True)
        df.to_csv(self.cadastro_arquivo, index=False)
        print("Paciente cadastrado com sucesso.")

    def registrar_diagnostico(self, nome_paciente, data_diagnostico, descricao, recomendacoes):
        df = pd.read_csv(self.diagnostico_arquivo)
        df = df.append({'Nome_Paciente': nome_paciente, 'Data_Diagnostico': data_diagnostico, 'Descricao': descricao, 'Recomendacoes': recomendacoes}, ignore_index=True)
        df.to_csv(self.diagnostico_arquivo, index=False)
        print("Diagnóstico registrado com sucesso.")

    def acompanhar_tratamento(self, nome_paciente, medicamentos, procedimentos, terapias):
        df = pd.read_csv(self.tratamento_arquivo)
        df = df.append({'Nome_Paciente': nome_paciente, 'Medicamentos': medicamentos, 'Procedimentos': procedimentos, 'Terapias': terapias}, ignore_index=True)
        df.to_csv(self.tratamento_arquivo, index=False)
        print("Tratamento acompanhado com sucesso.")

    def documentar_evolucao(self, nome_paciente, data, mudancas, resultados_exames, observacoes):
        df = pd.read_csv(self.evolucao_arquivo)
        df = df.append({'Nome_Paciente': nome_paciente, 'Data': data, 'Mudancas': mudancas, 'Resultados_Exames': resultados_exames, 'Observacoes': observacoes}, ignore_index=True)
        df.to_csv(self.evolucao_arquivo, index=False)
        print("Evolução documentada com sucesso.")

    def anexar_documento(self, nome_paciente, tipo_documento):
        df = pd.read_csv(self.anexos_arquivo)
        df = df.append({'Nome_Paciente': nome_paciente, 'Tipo_Documento': tipo_documento}, ignore_index=True)
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
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")
