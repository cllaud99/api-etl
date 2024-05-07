from spotify_requests import fetch_artists_data
from artists import joao_rock
from schemas import Artist, Album
from db_operations import df_to_database, execute_sql_file, execute_sql_file_to_dict
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

    # schema_artists = Artist
    # festival_data = joao_rock.get_all_spotify_links()
    #data = fetch_artists_data(festival_data, schema_artists)
    #consulta_palcos = joao_rock.get_dataframe()

    #df_to_database('stages_and_artists', consulta_palcos, 'bronze')
    #df_to_database('spotify_artist', data, 'bronze')

    dict_ids_artists = execute_sql_file_to_dict('sql/get_id_artists.sql')
    ids = [d['id'] for d in dict_ids_artists]
    print(ids)
    schema_album = Album
    albums_data = fetch_artists_data(ids, schema_album)
    debug = df_to_database('spotify_albums', albums_data, 'bronze')
    print(debug)
    print(albums_data.columns)

    

