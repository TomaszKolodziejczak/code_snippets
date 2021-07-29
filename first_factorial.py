"""
First Factorial

Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example:
 if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between
 1 and 18 and the input will always be an integer.
Examples

Input: 4
Output: 24
Input: 8
Output: 40320
"""


def first_factorial(num):
    if num == 0:
        return 1
    return num * first_factorial(num-1)


if __name__ == "__main__":
    print(first_factorial(4))
