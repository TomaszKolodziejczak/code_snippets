from typing import Union, List, Tuple


def is_palindrom(text: str) -> bool:
    # this function returns True if string is palindrom or False if it's not
    text = text.lower().replace(',', '').strip()
    return text == text[::-1]
