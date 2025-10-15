import pandas as pd

aditivos_df = pd.read_excel("C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\planilha_aditivos.xlsx")
principais_df = pd.read_excel("C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\planilha_documentos_principais.xlsx")

# Verificar se a primeira coluna de aditivos e principais tem o mesmo tipo de dado
aditivos_df['Número do Contrato'] = aditivos_df.iloc[:, 0].astype(str) # Inserir o nome da coluna da planilha que será usado para comparação
principais_df['Número do Contrato'] = principais_df.iloc[:, 0].astype(str) # Inserir o nome da coluna da planilha que será usado para comparação

for i, row_aditivos in aditivos_df.iterrows():
    valor_aditivo = row_aditivos['Número do Contrato']
    if valor_aditivo in principais_df['Número do Contrato'].values:
        # Encontrar a linha correspondente em principais
        linha_principal = principais_df[principais_df['Número do Contrato'] == valor_aditivo]
        # Obter o valor
        valor_coluna = linha_principal.iloc[0, 8] # Inserir aqui o numero da coluna que contem o id do documento principal

        coluna_com_id_principal = 9 # Inserir aqui o numero da coluna que irá receber o valor do documento principal
        aditivos_df.at[i, aditivos_df.columns[coluna_com_id_principal]] = valor_coluna

aditivos_df.to_excel('C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\planilha_aditivos_atualizada.xlsx', index=False)

print("Processamento concluído. A planilha de aditivos foi atualizada.")