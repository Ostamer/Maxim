from config import VALID_QUERY_PARAM_WITH_FILTER, VALID_QUERY_PARAM
from constants import ASSERT_MESSAGES
from models import Artwork, ArtworkList
from utils import get_artwork_by_id, search_artworks_with_query


def test_search_artworks_by_query_with_filters():
    """
    Тест получения существующих произведений искусства по ключевому слову с фильтрацией

    Ожидаемый результат:
    код статуса 200
    у всех найденных произведений поле isHighlight имеет значение True
    """
    # Получение списка произведений с фильтрацией
    response = search_artworks_with_query(VALID_QUERY_PARAM_WITH_FILTER)

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

    # Итерация по всем полученным произведениям
    for object_id in artwork_list.objectIDs:
        # Получение объекта по id
        resp = get_artwork_by_id(object_id)

        # Проверка корректности полученного статуса запроса
        assert resp.status_code == 200, ASSERT_MESSAGES["status_200"].format(
            status=resp.status_code
        )

        # Получение данных из запроса
        artwork_data = resp.json()

        # Распаковка словаря с данными
        artwork = Artwork(**artwork_data)

        # Проверка поля isHighlight, имеет значение True
        assert artwork.isHighlight is True, (
            ASSERT_MESSAGES["check_field_isHighLight"].format(
                isHighLight=artwork.isHighlight
            )
        )


def test_search_results_limit():
    """
    Тест ограничения количества возвращаемых результатов поиска

    Ожидаемый результат:
    длина списка objectIDs меньше или равна значению total
    """
    # Получение списка произведений с фильтрацией
    response = search_artworks_with_query(VALID_QUERY_PARAM)

    # Получение данных из запроса
    data = response.json()

    # Проверка, что поле objectIDs существует
    if data.get("objectIDs") is None:
        data["objectIDs"] = []

    # Распаковка словаря с данными
    artwork_list = ArtworkList(**data)

    # Проверка, что количество возвращённых ID не превышает общее число найденных
    assert len(artwork_list.objectIDs) <= artwork_list.total, (
        ASSERT_MESSAGES["objectIDs_less_or_equal_total"].format(
            count=len(artwork_list.objectIDs), total=artwork_list.total
        )
    )
