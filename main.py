import time
from app.config import CONFIG
from app.document_processor import DocumentProcessor
from app.api_client import ApiClient

def main():
    """Ponto de entrada principal do script."""
    print("--- INICIANDO PROCESSO DE VINCULAÇÃO DE DOCUMENTOS ---")
    
    try:
        # 1. Processamento da Planilha
        processor = DocumentProcessor(CONFIG)
        processor.load_data()
        processor.process_and_split_documents()
        payloads = processor.generate_api_payloads()

        if not payloads:
            print("\nNenhum documento para vincular. Encerrando.")
            return

        # 2. Vinculação via API
        print("\nPASSO 5: Iniciando vinculação via API...")
        api = ApiClient(url=CONFIG["api_url"], token=CONFIG["api_token"])
        
        total = len(payloads)
        respostas = []
        for i, payload in enumerate(payloads):
            print(f"  - Vinculando {i+1}/{total}: Aditivo ID {payload['doc_id']} -> Principal ID {payload['id_principal']}")
            resposta = api.link_document(payload)
            respostas.append(resposta)
            time.sleep(CONFIG["tempo_espera_segundos"])

        print("\n--- PROCESSO FINALIZADO ---")
        print("Respostas da API:")
        for resp in respostas:
            print(f"  -> {resp}")

    except (ValueError, FileNotFoundError) as e:
        print(f"\nERRO: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()