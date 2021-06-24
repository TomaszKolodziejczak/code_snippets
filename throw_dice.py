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
    set_min_val = int(input("Enter min value you want to get: "))
    set_max_val = int(input("Enter max value you want to get: "))

    dice = Dice(set_min_val, set_max_val)
    print(dice)

    steps = dice.throw()
    print(f'You can move {steps} steps forward')
