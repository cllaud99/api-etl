import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import logging
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

def df_to_database(table_name, df, schema='public'):
    """
    Função para armazenar um DataFrame em um banco PostgreSQL.
    
    Args:
        database_uri (str): URI para conexão com o banco de dados.
        table_name (str): Nome da tabela destino.
        df (pd.DataFrame): DataFrame que será armazenado.
        
    Returns:
        str: Mensagem de sucesso ou erro.
    """

    if df.empty:
        return "DataFrame está vazio, nada para armazenar."

    try:
        engine = create_engine(DATABASE_URI, echo=True)
        print("Conexão criada")
    except SQLAlchemyError as e:
        return f"Erro ao conectar ao banco de dados: {type(e).__name__}: {str(e)}"

    # Tenta armazenar os dados no banco de dados
    try:
        with engine.begin() as connection:
            df.to_sql(name=table_name, con=connection, if_exists='replace', index=False, schema=schema)
            print("Estamos no with")
        return f"Dados armazenados com sucesso na tabela '{table_name}'."
    except SQLAlchemyError as e:
        return f"Erro ao armazenar dados no banco: {type(e).__name__}: {str(e)}"
    except Exception as e:
        return f"Erro inesperado: {type(e).__name__}: {str(e)}"
    
def execute_sql_file(sql_file_path):
    try:

        engine = create_engine(DATABASE_URI)
        
        with open(sql_file_path, 'r') as f:
            sql = f.read() 
        
        with engine.begin() as connection: 

            connection.execute(text(sql))
            print("Comando SQL do arquivo executado com sucesso")
    
    except SQLAlchemyError as e:

        print("Erro ao executar comando SQL:", str(e))
    except FileNotFoundError:

        print(f"Arquivo '{sql_file_path}' não encontrado")
    except Exception as e:

        print("Erro inesperado:", str(e))