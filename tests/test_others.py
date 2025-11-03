from config import VALID_QUERY_PARAM_WITH_FILTER, VALID_QUERY_PARAM
from models import Artwork, ArtworkList
from utils import get_artwork_by_id, search_artworks_with_query


# Тест получения существующих произведений искусств по ключевому слову с филтрацией
def test_search_artworks_by_query_with_filters():
    response = search_artworks_with_query(VALID_QUERY_PARAM_WITH_FILTER)
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
    response = search_artworks_with_query(VALID_QUERY_PARAM)
    data = response.json()

    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    artwork_list = ArtworkList(**data)
    assert len(artwork_list.objectIDs) <= artwork_list.total
