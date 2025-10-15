import pandas as pd

planilha_docs_principais = pd.read_excel("C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\planilha_documentos_principais.xlsx")
planilha_todos_docs = pd.read_excel("C:\\Users\\NETLEX\\Desktop\\Legado - Vinculação de documento\\Planilha Versão Final.xlsx")

# Compara as duas planilhas e cria a planilha com as linhas que não existem na planilha de documentos principais
diferenca = planilha_todos_docs[~planilha_todos_docs.apply(tuple, 1).isin(planilha_docs_principais.apply(tuple, 1))]
diferenca.to_excel('planilha_aditivos.xlsx', index=False)

print("Processo concluído. A diferença foi salva em planilha_aditivos.xlsx")
