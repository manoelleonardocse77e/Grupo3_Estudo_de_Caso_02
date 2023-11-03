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
