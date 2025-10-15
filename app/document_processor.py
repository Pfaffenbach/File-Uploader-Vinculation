import pandas as pd
import os
import sys

class DocumentProcessor:
    """Processa a planilha para separar e enriquecer os dados dos documentos."""
    def __init__(self, config: dict):
        self.config = config
        self.df_completo = None
        self.df_principais = None
        self.df_aditivos_final = None

    def load_data(self):
        """Carrega a planilha principal a partir do caminho configurado."""
        path = os.path.join(self.config["diretorio_dados"], self.config["arquivo_entrada"])
        print(f"PASSO 1: Carregando dados de '{path}'...")
        try:
            self.df_completo = pd.read_excel(path)
            if self.config["coluna_id_contrato"] is None:
                self.config["coluna_id_contrato"] = self.df_completo.columns[0]
            print(f"-> Planilha carregada. Usando '{self.config['coluna_id_contrato']}' como ID.")
        except FileNotFoundError:
            print(f"ERRO CRÍTICO: Arquivo de entrada não encontrado em '{path}'.")
            sys.exit(1)

    def process_and_split_documents(self):
        """Executa a separação de documentos principais e aditivos e preenche os IDs."""
        if self.df_completo is None:
            raise ValueError("Os dados não foram carregados. Chame o método load_data() primeiro.")

        print("PASSO 2: Separando documentos principais e aditivos...")
        id_col = self.config["coluna_id_contrato"]
        
        df_principais = self.df_completo.drop_duplicates(subset=[id_col], keep='first').copy()
        
        merged = self.df_completo.merge(df_principais, how='left', indicator=True)
        df_aditivos = self.df_completo[merged['_merge'] == 'left_only'].copy()
        
        print(f"-> Encontrados {len(df_principais)} principais e {len(df_aditivos)} aditivos.")

        print("PASSO 3: Preenchendo IDs dos principais nos aditivos...")
        id_doc_col = self.config["coluna_id_documento"]
        id_principal_col = self.config["coluna_id_principal_no_aditivo"]
        
        principais_ids = df_principais[[id_col, id_doc_col]].rename(columns={id_doc_col: id_principal_col})
        self.df_aditivos_final = pd.merge(df_aditivos, principais_ids, on=id_col, how='left')

        # Salvar arquivos de saída
        self._save_dataframe(df_principais, self.config["arquivo_principais"])
        self._save_dataframe(self.df_aditivos_final, self.config["arquivo_aditivos_final"])

    def generate_api_payloads(self) -> list[dict]:
        """Gera a lista de dicionários (payloads) para enviar à API."""
        if self.df_aditivos_final is None:
            raise ValueError("Os documentos não foram processados. Chame process_and_split_documents() primeiro.")
        
        print("PASSO 4: Preparando dados para a API...")
        id_principal_col = self.config["coluna_id_principal_no_aditivo"]
        id_doc_col = self.config["coluna_id_documento"]

        self.df_aditivos_final.dropna(subset=[id_principal_col], inplace=True)
        
        payloads = self.df_aditivos_final.rename(columns={
            id_principal_col: "id_principal",
            id_doc_col: "doc_id"
        })[["id_principal", "doc_id"]].to_dict('records')
        
        print(f"-> {len(payloads)} documentos prontos para serem vinculados.")
        return payloads

    def _save_dataframe(self, df: pd.DataFrame, filename: str):
        """Função auxiliar para salvar um DataFrame na pasta de dados."""
        path = os.path.join(self.config["diretorio_dados"], filename)
        df.to_excel(path, index=False)
        print(f"-> Planilha '{filename}' salva em '{self.config['diretorio_dados']}'.")