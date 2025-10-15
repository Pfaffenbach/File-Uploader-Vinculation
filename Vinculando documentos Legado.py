import pandas as pd
import datetime
from openpyxl import load_workbook, Workbook
import requests
import os
import time
import json

request_url = "URL_DA_API"
my_headers = {
    'Authorization' : 'Bearer ' + 'TOKEN_DA_API',
    'Content-Type' : 'application/json'
}

def gerar_lista_dicionarios(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    
    lista_dicionarios = []
    
    # Itera sobre cada linha da planilha
    for index, row in df.iterrows():
        dicionario = {
            "id_principal": row["Document ID - Principal"],# Inserir aqui sempre a coluna que indica o id do documento principal
            "doc_id": row["Document ID"]# Inserir aqui sempre a coluna que indica o id do documento a ser vinculado ao principal
        }
        lista_dicionarios.append(dicionario)
    
    return lista_dicionarios

caminho_arquivo = "C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\planilha_aditivos_atualizada.xlsx"

dicionarios = gerar_lista_dicionarios(caminho_arquivo)

retornos = []
for dicionario in dicionarios:
    response = requests.post(request_url, json=dicionario, headers=my_headers, timeout=580).json()
    print(response)
    retornos.append(response)
    time.sleep(2)

print(retornos)