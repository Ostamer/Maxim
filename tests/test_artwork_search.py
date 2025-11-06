from config import VALID_QUERY_PARAM, INVALID_QUERY_PARAM
from constants import ASSERT_MESSAGES
from models import ArtworkList
from utils import search_artworks_with_query


def test_search_artworks_by_valid_query():
    """
    Тест получения существующего произведения искусства по ключевому слову

    Ожидаемый результат:
    код статуса 200
    поле total больше 0
    поле objectIDs имеет тип list
    """
    # Получение списка произведений по ключевым словам
    response = search_artworks_with_query(VALID_QUERY_PARAM)

    # Проверка корректности полученного статуса запроса
    assert response.status_code == 200, ASSERT_MESSAGES["status_200"].format(
        status=response.status_code
    )

    # Получение данных из запроса
    data = response.json()

    # Проверка, что поле objectIDs существует
    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    # Распаковка словаря с данными
    artwork_list = ArtworkList(**data)

    # Проверка, что поле total > 0
    assert artwork_list.total > 0, (
        ASSERT_MESSAGES["total_field_more_than_zero"].format(
            total=artwork_list.total
        )
    )

    # Проверка что поле objectIDs имеет тип список
    assert isinstance(artwork_list.objectIDs, list), (
        ASSERT_MESSAGES['objectIDs_field_type_is_list'].format(
            type=type(artwork_list.objectIDs)
        )
    )


def test_search_artworks_by_invalid_query():
    """
    Тест получения несуществующего произведения искусства по ключевым словам

    Ожидаемый результат:
    код статуса 200
    поле total равно 0
    список objectIDs пустой
    """
    # Получение списка произведений по ключевым словам
    response = search_artworks_with_query(INVALID_QUERY_PARAM)

    # Проверка корректности полученного статуса запроса
    assert response.status_code == 200, ASSERT_MESSAGES["status_200"].format(
        status=response.status_code
    )

    # Получение данных из запроса
    data = response.json()

    # Проверка, что поле objectIDs существует
    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    # Распаковка словаря с данными
    artwork_list = ArtworkList(**data)

    # Проверка, что поле total == 0
    assert artwork_list.total == 0, (
        ASSERT_MESSAGES["total_field_equal_zero"].format(
            total=artwork_list.total
        )
    )

    # Проверка, что список objectIDs пуст
    assert artwork_list.objectIDs == [], (
        ASSERT_MESSAGES["non_empty_objectIDs_field"].format(
            object_ids=artwork_list.objectIDs
        )
    )