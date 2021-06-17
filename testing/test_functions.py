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


@pytest.mark.parametrize("entry, expected", [
    ({
        'number': '678967896'
    },   '+48 678-967-896'),
    ({
        'number': '123123123',
        'area_code': '+1'
    },  '+1 123-123-123'),
    ({
        'number': '456654456',
        'area_code': '+123',
        'delimeter': '/',
    },   '+123 456/654/456')
])
def test_format_phone_number_advanced(entry, expected):
    assert format_phone_number(**entry) == expected
