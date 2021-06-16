import pytest
from functions import is_palindrom


@pytest.mark.parametrize("test_input,expected", [
    ('ala', True),
    ('level  ', True),
    ('LEVel,', True),
    ('Cat', True),

])
def test_is_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected
