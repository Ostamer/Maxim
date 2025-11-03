import pytest
from pydantic import ValidationError

from models import Artwork
from utils import get_artwork_by_id


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
