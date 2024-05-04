import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

def df_to_database(table_name, df):
    """
    Função que recebe um dataframe e armazena os dados em um banco PostgreSQL:
    Args:
        DATABASE_URI (str): cadeia de caracteres para conectar no banco de dados
        table_name (str): nome da tabela destino
        df (pd.DataFrame): dataframe que será armazenado
    Returns:
        str: mensagem de sucesso ou erro
    """
    try:

        engine = create_engine(DATABASE_URI)

        with engine.begin() as connection:
            df.to_sql(name=table_name, con=connection, if_exists='replace', index=False)

        return f"Dados armazenados com sucesso na tabela '{table_name}'."

    except SQLAlchemyError as e:
        return f"Erro ao armazenar dados: {str(e)}"

    except Exception as e:
        return f"Erro inesperado: {str(e)}"
    

def execute_sql_script(script_path):
    """
    Função que executa um script SQL a partir de um arquivo.
    
    Args:
        script_path (str): Caminho do arquivo de script SQL.
    
    Returns:
        str: Mensagem de sucesso ou erro.
    """

    engine = create_engine(DATABASE_URI)
    
    with open(script_path, 'r') as file:
        sql_script = file.read()

        print(sql_script)

    with engine.connect() as connection:

        try:
            connection.execute(text(sql_script))
            return f"Script '{script_path}' executado com sucesso."
        except Exception as e:
            return f"Erro ao executar o script: {e}"

    return "Terminou"
