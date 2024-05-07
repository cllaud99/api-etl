from spotify_requests import fetch_artists_data
from artists import joao_rock
from schemas import Artist
from db_operations import df_to_database, execute_sql_file
from transform import prepare_data_for_insertion
import pandas as pd
import os


db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


if __name__ == "__main__":
    schema = Artist
    festival_data = joao_rock.get_all_spotify_links()
    data = fetch_artists_data(festival_data, schema)
    print(data.dtypes)
    print(data)
    teste = df_to_database('spotify_artist', data, 'bronze')
    print(teste)

