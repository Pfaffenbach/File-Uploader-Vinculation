import pandas as pd

file_path = "C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\Planilha Versão Final.xlsx"
df = pd.read_excel(file_path)

# Coluna que será usada como base da vinculação
coluna_id = df.columns[0]

# Remover linhas duplicadas, mantendo apenas a primeira ocorrência de cada ID
# Lógica considerada é que a primeira ocorrencia da informação é o documento principal
df_unique = df.drop_duplicates(subset=[coluna_id], keep='first')

# Salvar a nova planilha com as linhas únicas
df_unique.to_excel('planilha_documentos_principais.xlsx', index=False)

print("Planilha salva com sucesso!")
