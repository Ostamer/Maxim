import pytest
from pydantic import ValidationError

from config import VALID_OBJECT_ID, INVALID_OBJECT_ID
from constants import ASSERT_MESSAGES
from models import Artwork
from utils import get_artwork_by_id


# Тест получения существующего произведения искусства по ID
def test_get_artwork_by_correct_id():
    response = get_artwork_by_id(VALID_OBJECT_ID)
    assert response.status_code == 200, ASSERT_MESSAGES["status_200"].format(
        status=response.status_code
    )
    data = response.json()
    try:
        artwork = Artwork(**data)
        assert artwork.objectID == VALID_OBJECT_ID, (
            ASSERT_MESSAGES["id_doesnt_match"].format(
                actual=artwork.objectID, expected=VALID_OBJECT_ID
            )
        )
        assert artwork.title != "", ASSERT_MESSAGES["empty_field_title"]
        assert isinstance(artwork.isPublicDomain, bool), (
            ASSERT_MESSAGES["invalid_public_domain_field_type"].format(
                type=type(artwork.isPublicDomain)
            )
        )
        assert isinstance(artwork.isHighlight, bool), (
            ASSERT_MESSAGES["invalid_highlight_field_type"].format(
                type=type(artwork.isHighlight)
            )
        )
    except ValidationError as e:
        pytest.fail(ASSERT_MESSAGES['validation_model_error'].format(
            error=e
        ))


# Тест получения несуществующего произведения искусства по ID
def test_get_artwork_by_invalid_id():
    response = get_artwork_by_id(INVALID_OBJECT_ID)
    assert response.status_code == 404, ASSERT_MESSAGES['status_404'].format(
        status=response.status_code
    )
