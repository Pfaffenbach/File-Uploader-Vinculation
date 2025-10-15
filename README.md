# Processador e Vinculador de Documentos Legado
Este projeto automatiza o processo de leitura de uma planilha Excel contendo informações de documentos, separando-os em "principais" e "aditivos", e por fim, utilizando uma API para vincular cada aditivo ao seu respectivo documento principal.

## 📋 Funcionalidades
- Leitura de Planilhas: Carrega dados de um arquivo .xlsx.

- Separação Automática: Identifica documentos principais (a primeira ocorrência de um contrato) e os aditivos subsequentes.

- Enriquecimento de Dados: Adiciona o ID do documento principal em cada linha de aditivo correspondente para preparar a vinculação.

- Consumo de API: Itera sobre os aditivos e envia requisições POST para uma API, realizando a vinculação na plataforma de destino.

- Configuração Centralizada: Todas as variáveis (nomes de arquivos, colunas, chaves de API) são gerenciadas em um único arquivo de configuração.

- Estrutura Modular (POO): O código é organizado em classes com responsabilidades bem definidas, facilitando a manutenção e a escalabilidade.

## 📂 Estrutura do Projeto
O projeto é organizado na seguinte estrutura de pastas e arquivos para garantir a separação de responsabilidades:

    File-Uploader-Vinculation/
    |
    ├── main.py                     # 🚀 Ponto de entrada para executar a aplicação
    ├── requirements.txt            # 📦 Lista de dependências Python
    |
    ├── app/                        # 核心 Pacote principal da aplicação
    |   ├── __init__.py             # Transforma o diretório 'app' em um pacote
    |   ├── config.py               # ⚙️ Arquivo de configuração central
    |   ├── document_processor.py   # 📊 Classe com a lógica de manipulação de planilhas (Pandas)
    |   └── api_client.py           # ☁️ Classe dedicada a se comunicar com a API
    |
    └── data/                       # 🗂️ Pasta para armazenar as planilhas
        └── Planilha Versão Final.xlsx

## 🛠️ Pré-requisitos
Python 3.8 ou superior.

Acesso à internet para baixar as dependências e se comunicar com a API.

## ⚙️ Instalação
Siga estes passos para configurar o ambiente de desenvolvimento local.

Clone o repositório (ou baixe e descompacte os arquivos):

```Bash
    git clone https://github.com/Pfaffenbach/File-Uploader-Vinculation.git
    cd File-Uploader-Vinculation
```

Instale as dependências listadas no requirements.txt:

```Bash
    pip install -r requirements.txt
```

## 🔧 Configuração Essencial
Antes de executar o script, você precisa realizar as seguintes configurações:

Adicione a Planilha: Coloque sua planilha principal (ex: Planilha Versão Final.xlsx) dentro da pasta data/.

Edite o Arquivo de Configuração: Abra o arquivo app/config.py e altere os seguintes valores:

- api_url: Substitua "URL_DA_API_AQUI" pela URL real da sua API.

- api_token: Substitua "TOKEN_DA_API_AQUI" pelo seu token de autorização Bearer.

# Exemplo em app/config.py
    CONFIG = {
        # ... outras configurações

        # --- Configurações da API ---
        "api_url": "https://api.suaempresa.com/v1/documents/link", # SUBSTITUA PELA URL REAL
        "api_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",   # SUBSTITUA PELO SEU TOKEN REAL
        "tempo_espera_segundos": 2
    }

Você também pode ajustar outros parâmetros no mesmo arquivo, como os nomes das colunas (coluna_id_documento) e dos arquivos de saída, se necessário.

## ▶️ Como Executar
Com a configuração concluída, execute o script a partir da pasta raiz do projeto (File-Uploader-Vinculation/):

```Bash
    python main.py
```

O script exibirá o progresso de cada etapa no terminal. Ao final, os arquivos processados (planilha_documentos_principais.xlsx e planilha_aditivos_atualizada.xlsx) serão salvos na pasta data/.

## 🔄 O Fluxo de Trabalho
Ao ser executado, o script segue os seguintes passos:

- Carregamento: A classe DocumentProcessor carrega a planilha da pasta data/.

- Processamento e Divisão: Os documentos são separados em principais e aditivos. O ID do documento principal é mapeado e inserido nas linhas dos aditivos correspondentes.

- Geração de Payloads: Uma lista de dicionários é preparada para ser enviada à API.

- Vinculação via API: A classe ApiClient é instanciada e itera sobre a lista de payloads, enviando uma requisição para cada aditivo, com uma pausa entre as chamadas para evitar sobrecarga na API.

- Finalização: As respostas da API são impressas no terminal.