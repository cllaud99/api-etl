class FestivalJoaoRock:
    def __init__(self, festival_data):
        self.artistas = festival_data

    def get_artist_info(self, nome_artista):
        """Retorna informações do artista pelo nome."""
        return self.artistas.get(nome_artista.upper(), None)

    def get_artistas_by_palco(self, nome_palco):
        """Retorna uma lista de artistas que tocam em um determinado palco."""
        return [
            artista
            for artista, info in self.artistas.items()
            if info["palco"].lower() == nome_palco.lower()
        ]

    def get_all_artistas(self):
        """Retorna uma lista de todos os artistas no festival."""
        return list(self.artistas.keys())

    def get_all_palcos(self):
        """Retorna uma lista de todos os palcos no festival."""
        return list(set(info["palco"] for info in self.artistas.values()))

    def get_all_artistas_by_palco(self):
        """Retorna um dicionário de palcos para listas de artistas."""
        artistas_por_palco = {}
        for artista, info in self.artistas.items():
            palco = info["palco"]
            if palco not in artistas_por_palco:
                artistas_por_palco[palco] = []
            artistas_por_palco[palco].append(artista)
        return artistas_por_palco
    
    def get_all_spotify_links(self):
        """Retorna uma lista de todas as URLs do Spotify dos artistas."""
        return [info["spotify_link"] for info in self.artistas.values()]

    def get_spotify_links_by_palco(self, nome_palco):
        """Retorna um dicionário de URLs do Spotify agrupadas por palco."""
        links_por_palco = {}
        for artista, info in self.artistas.items():
           palco = info["palco"]
           if palco.lower() == nome_palco.lower():
                if palco not in links_por_palco:
                    links_por_palco[palco] = []
                links_por_palco[palco].append(info["spotify_link"])
        return links_por_palco



festival_joao_rock = {
    "EMICIDA": {"spotify_link": '2d9LRvQJnAXRijqIJDDs2K?si=-hJGN7uTQoKiwvUKmvQRMw', "palco": "João Rock"},
    "PITTY": {"spotify_link": '2dmQ0vMD3THLMcz7DsvfaT?si=nPXt3rUmQw64cjZwNGMTmg', "palco": "João Rock"},
    "MARINA SENA": {"spotify_link": '0nFdWpwl7h6fp3ADRyG14L?si=_oW8v44VRX2gqqc1Teqm6g', "palco": "João Rock"},
    "OS PARALAMAS DO SUCESSO": {"spotify_link": '7EM9m7HOXxVgP9oEpDDv70?si=ycMi8hBERHuhdancBgUYJw', "palco": "João Rock"},
    "ARMANDINHO": {"spotify_link": '3h7RaVXBvdSNa7LXQtVYqH?si=wK4HKLyJSXiNs1mfukXPig', "palco": "João Rock"},
    "SAMUEL ROSA": {"spotify_link": '4fp0N4WchcumIW5HNGpPwa?si=ooCwYKIsQu-BVK_gXDI51A', "palco": "João Rock"},
    "CPM22": {"spotify_link": '2Jw4Lrfjnyv2QsDoBgnrAP?si=aKG5NwozSdytL8j8khJghQ', "palco": "João Rock"},
    "MARCELO D2": {"spotify_link": '1vEN3d3dJbmdHQpXD6AIkL?si=nsYCGphGSnatE7XuR6nR1Q', "palco": "João Rock"},
    "DJONGA": {"spotify_link": '204IwDdaHE4ymGk9Kya2pY?si=WMddTUVTS7qYYMub8uWWJw', "palco": "João Rock"},
    "DETONAUTAS": {"spotify_link": '5AlUDdksfPP7l4Qm22MJA9?si=TRSHbeC6QCyc4ZZIGfmjoQ', "palco": "João Rock"},
    "BATALHA DA ALDEIA": {"spotify_link": '5ZLMlQ5WInZPXv6eTmqQiJ?si=CYbrIVWKQSWZZAntKo7f8g', "palco": "João Rock"},
    "MARÇÃO BRITTO": {"spotify_link": '5jKJ8fkQJwbAb8z0cFpaWe?si=G1D80Y2kRIi_L4WHx6GN6g', "palco": "João Rock"},
    "THIAGO CASTANHO": {"spotify_link": '0r7OBphuxWbq7yxyDmalER?si=973fa78c2099494d', "palco": "João Rock"},

    "MARIA GADÚ": {"spotify_link": "3uCu2WgyG0Iw50ylOYDSpH?si=0a53a8329cd94023", "palco": "Aquarela"},
    "MARINA LIMA": {"spotify_link": "28IcRPf399RPv4TUiZ7uol?si=UhSve95wRpenF9FaXhoZFw", "palco": "Aquarela"},
    "TÁSSIA REIS": {"spotify_link": "0kc1BjcLHaXhZVzCp0HeAl?si=6b7525a1a1aa4a49", "palco": "Aquarela"},
    "NEGRA LI": {"spotify_link": "1E4r5qziZja6v8jA7iTqjn?si=lwtyXg5tRa6doDs9cHyGMA", "palco": "Aquarela"},
    "DUDA BEAT": {"spotify_link": "2QLSJqqGIstNbO6nYRR16o?si=f10f653f3f1743df", "palco": "Aquarela"},

    "LULU SANTOS": {"spotify_link": "0A1oy7PC7fdzURgaLaWkL1?si=80ddbffab7d24c80", "palco": "Brasil Lendas Vol. 2"},
    "DJAVAN": {"spotify_link": "5rrmaoBXZ7Jcs4Qb77j0YA?si=83dff372b004446f", "palco": "Brasil Lendas Vol. 2"},
    "NEY MATOGROSSO": {"spotify_link": "2SFIMUkCdZowbeisskDdhn?si=f5e5baf8a86a4396", "palco": "Brasil Lendas Vol. 2"},
    "14 BIS": {"spotify_link": "4cz8toptnAtxffn7ghNjyp?si=b0e134ad70ba46bd", "palco": "Brasil Lendas Vol. 2"},
    "NOVOS BAIANOS": {"spotify_link": "2ohBjgFT9V0LRDWO2wF9DJ?si=a7535449f5b6499f", "palco": "Brasil Lendas Vol. 2"},

    "VEIGH": {"spotify_link": '4YqwRbMLqGHRHLS1w2ZKse?si=f649edbbf6a74ed6', "palco": "Fortalecendo a Cena"},
    "WIU": {"spotify_link": "3MrDVzg7ZXaYMyQmbDInr7?si=8f5c7cc09d0b4817", "palco": "Fortalecendo a Cena"},
    "TETO": {"spotify_link": "68YeXpLt3jB7JHQS5ZjMGo?si=8e4163c2988144bc", "palco": "Fortalecendo a Cena"},
    "EBONY": {"spotify_link": "1UBSRfDGNkhpTWQeMyCwHb?si=126172e10aeb4c96", "palco": "Fortalecendo a Cena"},
    "RYU THE RUNNER": {"spotify_link": "1ZzJx2AgPmbnOE6OXhnn5K?si=dc47cdc4e9d4421a", "palco": "Fortalecendo a Cena"},
}


joao_rock = FestivalJoaoRock(festival_joao_rock)

# Exemplo de uso
print("Informações do artista EMICIDA:", joao_rock.get_all_spotify_links())
#print("Artistas no palco João Rock:", joao_rock.get_artistas_by_palco("João Rock"))
#print("Todos os artistas:", joao_rock.get_all_artistas())
#print("Todos os palcos:", joao_rock.get_all_palcos())
#print("Artistas por palco:", joao_rock.get_all_artistas_by_palco())