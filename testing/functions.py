from textwrap import wrap
from typing import Union, List, Tuple


def is_palindrom(text: str) -> bool:
    # this function returns True if string is palindrom or False if it's not
    text = text.lower().replace(',', '').strip()
    return text == text[::-1]


def format_phone_number(number: str, area_code: str = '+48', delimeter: str = '-') -> str:
    wrapped_number = delimeter.join(wrap(number, 3))
    return f"{area_code} {wrapped_number}"


if __name__ == "__main__":
    data = {
        'number': '456654456',
        'area_code': '+123',
        'delimeter': '/',
    }
    print(format_phone_number(**data))
