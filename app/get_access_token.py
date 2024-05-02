import pandas as pd
import requests
import base64
import os
from dotenv import load_dotenv


def convert_str_to_base64(string: str) -> str:
    """
    Converte uma string ASCII para Base64.
    Args:
        string (str): A string a ser convertida.
    Returns:
        str: A versão em Base64 da string.
    """
    string_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')
    return base64_string


def access_token() -> str:
    
    """
    Obtém um token de acesso do Spotify usando autenticação básica.
    
    Args:
        Nenhum argumento é necessário, mas usa variáveis de ambiente para obter
        `client_id` e `client_secret`.

    Returns:
        str: O token de acesso recebido do Spotify.
    """
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    client_id_and_client_secret = client_id + ':' + client_secret
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {convert_str_to_base64(client_id_and_client_secret)}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=payload)
    
    return response.json().get('access_token')

if __name__ == "__main__":
    token = access_token()
    print(token)