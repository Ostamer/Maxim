from models import ArtworkList
from utils import search_artworks_with_query


# Тест получения существующего произведения искусства по ключевому слову
def test_search_artworks_by_valid_query():
    response = search_artworks_with_query("Scream")
    assert response.status_code == 200
    data = response.json()

    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    artwork_list = ArtworkList(**data)
    assert artwork_list.total > 0
    assert isinstance(artwork_list.objectIDs, list)


# Тест получения несуществующего произведения искусства по ключевому слову
def test_search_artworks_by_invalid_query():
    response = search_artworks_with_query("Anigilation")
    assert response.status_code == 200
    data = response.json()

    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    artwork_list = ArtworkList(**data)
    assert artwork_list.total == 0
    assert artwork_list.objectIDs == []