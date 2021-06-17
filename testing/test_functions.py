import pytest
from functions import is_palindrom, format_phone_number


@pytest.mark.parametrize("test_input,expected", [
    ('ala', True),
    ('level  ', True),
    ('LEVel,', True),
    ('Cat', True),

])
def test_is_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected


def test_format_phone_number():
    data = {
        'delimeter': '_',
        'number': '444555666',
        'area_code': '+49',
    }
    assert format_phone_number(**data) == '+49 444_555_666'
