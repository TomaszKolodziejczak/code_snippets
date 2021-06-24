from random import randint

"""Write a program that simulates the throw of a dice"""


# solution 1
result = randint(1, 6)


# solution 2
class Dice:

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f'This dice returns result between {self.min_value} and {self.max_value}'

    def throw(self):
        return randint(self.min_value, self.max_value)


if __name__ == "__main__":
    # solution 1
    print(result)

    # solution 2
    d = Dice(1, 6)
    print(d)
    steps = d.throw()
    print(f'You can move {steps} steps forward')
