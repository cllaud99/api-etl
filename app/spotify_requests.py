from get_access_token import access_token
import pandas as pd
from schemas import Artist
from pydantic import ValidationError, BaseModel, HttpUrl, AnyUrl
import requests
from typing import Optional
from artists import joao_rock


def has_nested(data):
    if isinstance(data, dict) or isinstance(data, list):
        return True
    return False

def recursive_normalize(df):
    while True:
        # Encontra todas as colunas que contêm dados aninhados
        nested_cols = [col for col in df.columns if df[col].apply(has_nested).any()]
        print("rodou recursive")
        if not nested_cols:
            break 
        
        for col in nested_cols:

            df_normalized = pd.json_normalize(df[col])
            df_normalized.columns = [f"{col}_{c}" for c in df_normalized.columns]
            df = pd.concat([df, df_normalized], axis=1).drop(columns=[col])
    
    return df

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
        validated_data = schema(**data)

        df = pd.DataFrame([validated_data.dict()])


        def flatten(value):
            if isinstance(value, AnyUrl):
                return str(value) 
            elif isinstance(value, list):

                return [flatten(item) for item in value]
            elif isinstance(value, dict):
                return {k: flatten(v) for k, v in value.items()}
            else:
                return value

        df = df.applymap(lambda x: flatten(x)) 

        if recursive_normalize:
            df = recursive_normalize(df)

        return df
    
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
        spotify_url = f'https://api.spotify.com/v1/artists/{link}/albums'

        print(spotify_url)

        artist_df = get_data_to_df(spotify_url, schema)

        if artist_df is not None:
            all_artists_df = pd.concat([all_artists_df, artist_df], ignore_index=True)
            all_artists_df['created_at'] = pd.Timestamp.now()

    return all_artists_df





if __name__ == "__main__":
    #spotify_link = '0Ludmn78UAusTsNCXgICrN?si=iWhh0a1iS727nnUHiq2CpQ'
    schema = Artist
    festival_data = joao_rock.get_all_spotify_links()
    data = fetch_artists_data(festival_data, schema)
    print(data)