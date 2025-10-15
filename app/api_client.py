import requests

class ApiClient:
    """Cliente para interagir com a API de vinculação de documentos."""
    def __init__(self, url: str, token: str):
        if not url or "URL_DA_API" in url:
            raise ValueError("URL da API não foi configurada.")
        if not token or "TOKEN_DA_API" in token:
            raise ValueError("Token da API não foi configurado.")
            
        self.request_url = url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def link_document(self, payload: dict) -> dict:
        """
        Envia um único pedido de vinculação para a API.
        
        Args:
            payload (dict): Dicionário contendo {'id_principal': ..., 'doc_id': ...}.
            
        Returns:
            dict: A resposta da API em formato JSON ou um dicionário de erro.
        """
        try:
            response = requests.post(self.request_url, json=payload, headers=self.headers, timeout=30)
            response.raise_for_status()  # Lança um erro para respostas 4xx ou 5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"  -> Erro de API para payload {payload}: {e}")
            return {"error": str(e), "payload": payload}