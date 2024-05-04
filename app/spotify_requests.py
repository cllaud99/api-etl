from get_access_token import access_token
import pandas as pd
from schemas import Artist
from pydantic import ValidationError
import requests
from typing import Optional
from artists import joao_rock


spotify_link = '0Ludmn78UAusTsNCXgICrN?si=iWhh0a1iS727nnUHiq2CpQ'
schema = Artist


def get_data_to_df(spotify_link: str, schema):

    """
    Obtém dados do Spotify usando a API e valida com Pydantic.

    Args:
        url (str): URL para buscar os dados.
        schema (pydantic.BaseModel): Classe para validação de dados.

    Returns:
        Optional[schema]: Instância da classe se validação for bem-sucedida,
                          None se houver erro de validação.
    """

    url = f'https://api.spotify.com/v1/artists/{spotify_link}'

    acess_token = access_token()

    headers = {'Authorization': f'Bearer {acess_token}'}

    response = requests.get(url = url, headers = headers)

    if response.status_code != 200:
        print("Ocorreu um erro: ", response.status_code)
        return None
    
    data = response.json()
    
    try:
        validate_data = schema(**data)
        df = pd.DataFrame([validate_data.dict()])
        df_normalize = pd.json_normalize(df.to_dict(orient='records'))
        return df_normalize
    
    except ValidationError as ve:
        print("Erro de validação: ", ve)
        return None
    

print("Informações do artista EMICIDA:", joao_rock.get_all_spotify_links())

if __name__ == "__main__":
    data = get_data_to_df(spotify_link, schema)
    print(data)