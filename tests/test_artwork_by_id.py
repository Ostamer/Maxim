import pytest
from pydantic import ValidationError

from config import VALID_OBJECT_ID, INVALID_OBJECT_ID
from constants import ASSERT_MESSAGES
from models import Artwork
from utils import get_artwork_by_id


def test_get_artwork_by_correct_id():
    """
    Тест получения существующего произведения искусства по ID

    Ожидаемый результат:
    код статуса 200
    objectID совпадает с ожидаемым
    поле title не пустое
    поля isPublicDomain и isHighlight имеют тип bool
    """
    # Получение объекта по id
    response = get_artwork_by_id(VALID_OBJECT_ID)

    # Проверка корректности полученного статуса запроса
    assert response.status_code == 200, ASSERT_MESSAGES["status_200"].format(
        status=response.status_code
    )

    # Получение данных из запроса
    data = response.json()
    try:
        # Распаковка словаря с данными
        artwork = Artwork(**data)

        # Проверка корректности id полученного объекта
        assert artwork.objectID == VALID_OBJECT_ID, (
            ASSERT_MESSAGES["id_doesnt_match"].format(
                actual=artwork.objectID, expected=VALID_OBJECT_ID
            )
        )

        # Проверка поля title, что оно не является пустым
        assert artwork.title != "", ASSERT_MESSAGES["empty_field_title"]

        # Проверка поля isPublicDomain, что оно имеет тип bool
        assert isinstance(artwork.isPublicDomain, bool), (
            ASSERT_MESSAGES["invalid_public_domain_field_type"].format(
                type=type(artwork.isPublicDomain)
            )
        )

        # Проверка поля isHighlight, что оно имеет тип bool
        assert isinstance(artwork.isHighlight, bool), (
            ASSERT_MESSAGES["invalid_highlight_field_type"].format(
                type=type(artwork.isHighlight)
            )
        )

    # Проверка корректной валидности модели
    except ValidationError as e:
        pytest.fail(ASSERT_MESSAGES['validation_model_error'].format(
            error=e
        ))


def test_get_artwork_by_invalid_id():
    """
    Тест получения несуществующего произведения искусства по ID

    Ожидаемый результат:
    код статуса 404
    """
    # Получение объекта по id
    response = get_artwork_by_id(INVALID_OBJECT_ID)

    # Проверка корректности полученного статуса из запроса
    assert response.status_code == 404, ASSERT_MESSAGES['status_404'].format(
        status=response.status_code
    )
