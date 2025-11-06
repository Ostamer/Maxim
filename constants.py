# Сообщения для assert
ASSERT_MESSAGES = {
    'status_200': "Ожидаемый статус 200, получен статус {status}",
    'total_field_more_than_zero': (
        "Поле 'total' должно быть больше 0, "
        "получено значение {total}"
    ),
    'total_field_equal_zero': (
        "Поле 'total' должно быть равно 0, "
        "получено значение {total}"
    ),
    'objectIDs_field_type_is_list': (
        "Поле 'objectIDs' должно иметь тип список, "
        "а не тип {type}"
    ),
    'non_empty_objectIDs_field': (
        "Список objectIDS должен быть пустым, "
        "получены id: {object_ids}"
    ),
    'check_field_isHighLight': (
        "Ожидаемое значение поля isHighLight True, "
        "получено значение {isHighLight}"
    ),
    'objectIDs_less_or_equal_total': (
        "Количество найденных objectIDs ({count}) "
        "должно быть меньше или равно total ({total})"
    ),
    'status_404': "Ожидаемый статус 404, получен статус {status}",
    'id_doesnt_match': (
        "ID объекта не совпадает: ожидался id {expected}, "
        "получен id {actual}"
    ),
    'empty_field_title': "Поле 'title' пустое",
    'invalid_public_domain_field_type': (
        "Поле 'isPublicDomain' должно иметь тип bool, "
        "а не тип {type}"
    ),
    'invalid_highlight_field_type': (
        "Поле 'isHighlight' должно иметб тип bool, "
        "а не тип {type}"
    ),
    'validation_model_error': "Ошибка валидации модели Artwork: {error}"
}