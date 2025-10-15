import os

# Define o caminho base do projeto
# O 'os.path.dirname(__file__)' pega o diretório do arquivo atual ('app')
# O 'os.path.join(..., "..")' volta um nível para a raiz ('projeto_vinculacao')
BASE_DIR = os.path.join(os.path.dirname(__file__), "..")

CONFIG = {
    # --- Arquivos e Caminhos ---
    # Usamos os.path.join para garantir que os caminhos funcionem em qualquer sistema operacional
    "diretorio_dados": os.path.join(BASE_DIR, "data"),
    "arquivo_entrada": "Planilha Versão Final.xlsx",
    
    # Nomes dos arquivos de saída (serão salvos na pasta 'data')
    "arquivo_principais": "planilha_documentos_principais.xlsx",
    "arquivo_aditivos": "planilha_aditivos.xlsx",
    "arquivo_aditivos_final": "planilha_aditivos_atualizada.xlsx",

    # --- Nomes das Colunas ---
    # Deixe como None para detectar a primeira coluna automaticamente, ou defina um nome.
    "coluna_id_contrato": None, 
    "coluna_id_documento": "Document ID",
    "coluna_id_principal_no_aditivo": "Document ID - Principal",

    # --- Configurações da API ---
    "api_url": "URL_DA_API_AQUI", # SUBSTITUA PELA URL REAL
    "api_token": "TOKEN_DA_API_AQUI", # SUBSTITUA PELO SEU TOKEN REAL
    "tempo_espera_segundos": 2
}