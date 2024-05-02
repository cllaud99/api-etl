from get_access_token import access_token
import requests
from typing import Optional


url = 'https://api.spotify.com/v1/artists/0Ludmn78UAusTsNCXgICrN?si=iWhh0a1iS727nnUHiq2CpQ'


def get_artist_data(url: str, acess_token: str, schema):

    """
    Obtém dados de um artista do Spotify usando a API e valida com Pydantic.

    Args:
        artist_url (str): URL do artista na API do Spotify.
        access_token (str): Token de acesso para autenticação na API.
        schema (str) : esquema com os dados para validação.

    Returns:
        Optional[Artist]: Instância da classe Artist se validação for bem-sucedida,
                          None se houver erro de validação.
    """
    acess_token = access_token()

    headers = {'Authorization': f'Bearer {acess_token}'}

    response = requests.request('GET', url = url, headers=headers)

    print(response.content)