from get_access_token import access_token
import pandas as pd
from schemas import Artist
from pydantic import ValidationError
import requests
from typing import Optional
from artists import joao_rock



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

    acess_token = access_token()

    headers = {'Authorization': f'Bearer {acess_token}'}

    response = requests.get(url = spotify_link, headers = headers)

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
    
def fetch_artists_data(festival_data, schema):
    """
    Busca dados de artistas no Spotify usando links

    Args:
        festival_data (dict): Dicionário com dados dos artistas.
        schema (pydantic.BaseModel): Classe para validação de dados.

    Returns:
        pd.DataFrame: DataFrame com os dados dos artistas.
    """
    all_artists_df = pd.DataFrame()

    for link in festival_data:
        spotify_url = f'https://api.spotify.com/v1/artists/{link}'

        print(spotify_url)

        artist_df = get_data_to_df(spotify_url, schema)

        if artist_df is not None:
            all_artists_df = pd.concat([all_artists_df, artist_df], ignore_index=True)

    return all_artists_df



if __name__ == "__main__":
    #spotify_link = '0Ludmn78UAusTsNCXgICrN?si=iWhh0a1iS727nnUHiq2CpQ'
    schema = Artist
    festival_data = joao_rock.get_all_spotify_links()
    data = fetch_artists_data(festival_data, schema)
    print(data)