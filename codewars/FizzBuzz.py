def fizzbuzz(n):
    for i in range(1, n):
        result = ''

        if not i % 5:
            result += 'Fizz'

        if not i % 7:
            result += 'Buzz'

        if result:
            print(result)
        else:
            print(i)


if __name__ == '__main__':
    fizzbuzz(40)
