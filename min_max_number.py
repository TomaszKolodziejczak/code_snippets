from typing import List


def min_max_number(nums: List) -> str:
    minimum, maximum = None, None

    for num in nums:
        if maximum is None or maximum < num:
            maximum = num

        if minimum is None or minimum > num:
            minimum = num

    return f'minimum: {minimum}\nmaximum: {maximum}'


if __name__ == "__main__":
    nums = [17, -4, 6, 9, 12, -334, -2, 1, 44]
    print(min_max_number(nums))
