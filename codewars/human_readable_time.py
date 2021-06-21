"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

kata's author BattleRattle
"""


# solution 1
from symbol import test


def make_readable(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 - hours * 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


# solution 2
def make_readable2(seconds):
    return f"{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}"


if __name__ == "__main__":
    print(make_readable2(3620))

