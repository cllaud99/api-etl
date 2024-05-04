from spotify_requests import fetch_artists_data
from artists import joao_rock
from schemas import Artist
from db_operations import df_to_database, execute_sql_script

if __name__ == "__main__":
    execute_sql_script('sql/create_tables.sql')
    #spotify_link = '0Ludmn78UAusTsNCXgICrN?si=iWhh0a1iS727nnUHiq2CpQ'
    #schema = Artist
    #festival_data = joao_rock.get_all_spotify_links()
    #data = fetch_artists_data(festival_data, schema)
    #df_to_database ("artistas", data)

def test_connection():
    engine = create_engine(DATABASE_URI)
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            return "Conexão bem-sucedida"
    except Exception as e:
        return f"Erro ao conectar: {e}"

print(test_connection())