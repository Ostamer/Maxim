import pytest
from pydantic import ValidationError

from models import Artwork, ArtworkList
from utils import get_artwork_by_id, search_artworks_with_query


# Тест получения существующего произведения искусства по ID
def test_get_artwork_by_correct_id():
    response = get_artwork_by_id(436121)
    assert response.status_code == 200
    data = response.json()
    try:
        artwork = Artwork(**data)
        assert artwork.objectID == 436121
        assert artwork.title != ""
        assert isinstance(artwork.isPublicDomain, bool)
        assert isinstance(artwork.isHighlight, bool)
    except ValidationError as e:
        pytest.fail(f"Ошибка: {e}")


# Тест получения несуществующего произведения искусства по ID
def test_get_artwork_by_invalid_id():
    response = get_artwork_by_id(-200)
    assert response.status_code == 404


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

# Тест получения существующих произведений искусств по ключевому слову с филтрацией
def test_search_artworks_by_query_with_filters():
    response = search_artworks_with_query("Scream&isHighlight=true")
    assert response.status_code == 200
    data = response.json()
    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    artwork_list = ArtworkList(**data)

    for object_id in artwork_list.objectIDs:
        resp = get_artwork_by_id(object_id)
        assert resp.status_code == 200
        artwork_data = resp.json()
        artwork = Artwork(**artwork_data)
        assert artwork.isHighlight is True


# Тест ограничения на количество возвращаемых результатов
def test_search_results_limit():
    response = search_artworks_with_query("Scream")
    data = response.json()

    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    artwork_list = ArtworkList(**data)
    assert len(artwork_list.objectIDs) <= artwork_list.total

