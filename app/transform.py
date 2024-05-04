import json
from collections.abc import Iterable
from pydantic import AnyUrl
import pandas as pd

# Função para converter valores para formatos compatíveis com PostgreSQL
def convert_for_postgres(value):
    if isinstance(value, AnyUrl):
        # Converte objetos de URL para strings
        return str(value)
    elif isinstance(value, dict):
        # Converte dicionários para JSON
        return json.dumps({k: convert_for_postgres(v) for k, v in value.items()})
    elif isinstance(value, list):
        # Converte listas para uma lista de valores serializáveis
        return json.dumps([convert_for_postgres(v) for v in value])
    elif isinstance(value, Iterable) and not isinstance(value, str):
        # Converte outros iteráveis para uma lista de valores serializáveis
        return json.dumps([convert_for_postgres(v) for v in value])
    else:
        # Outros tipos são retornados como estão
        return value


# Função para preparar dados para inserção
def prepare_data_for_insertion(data):
    # Converte todos os valores para um formato compatível com PostgreSQL
    converted_data = {key: convert_for_postgres(value) for key, value in data.items()}
    df = pd.DataFrame([converted_data.dict()])
    df_normalize = pd.json_normalize(df.to_dict(orient='records'))
    return pd.DataFrame([converted_data])
