CREATE TABLE IF NOT EXISTS spotify_artist (
    genres TEXT[],  -- Um array de gêneros musicais associados ao artista
    href VARCHAR(255),  -- URL para o recurso do artista na API do Spotify
    id VARCHAR(50) PRIMARY KEY,  -- Identificador único do artista no Spotify
    name VARCHAR(100),  -- Nome do artista
    popularity INT,  -- Nível de popularidade do artista
    type VARCHAR(50),  -- Tipo do objeto, neste caso, 'artist'
    uri VARCHAR(100),  -- URI único do Spotify para o artista
    external_urls_spotify VARCHAR(255),  -- URL para o perfil do artista no site do Spotify
    followers_href VARCHAR(255),  -- URL para os dados dos seguidores (pode ser nulo)
    followers_total INT  -- Número total de seguidores do artista
);