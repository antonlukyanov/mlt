def keys_exist(dictionary, *keys):
    """
    Проверяет есть ли в словаре dictionary все (вложенные) ключи *keys.
    """
    if not isinstance(dictionary, dict):
        raise AttributeError('keys_exists() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('keys_exists() expects at least two arguments, one given.')

    _element = dictionary
    for key in keys:
        try:
            _element = _element[key]
        except KeyError:
            return False
    return True


def set_value(dictionary, value, *keys):
    """
    Добавляет в словарь dictionary вложенные ключи *keys.

    :param dictionary:
    :param keys:
    :param value:
    :return:
    """
    if not isinstance(dictionary, dict):
        raise AttributeError('set_value() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('set_value() expects at least two arguments, one given.')

    _element = dictionary
    for i, key in enumerate(keys):
        if i != len(keys) - 1:
            if key not in _element or not isinstance(_element[key], dict):
                _element[key] = {}
        else:
            _element[key] = value
        _element = _element[key]


def get_value(dictionary, *keys):
    if not isinstance(dictionary, dict):
        raise AttributeError('get_value() expects dict as first argument.')
    if len(keys) == 0:
        raise AttributeError('get_value() expects at least two arguments, one given.')

    _element = dictionary
    for key in keys:
        _element = _element[key]
    return _element
