from datetime import datetime


def loving_python(fn):
    def wrapper(*args, **kwargs):
        print('No matter what the function returns, let everyone know You love Python!')
        return fn(*args, **kwargs)
    return wrapper


def capitalise_text(fn):
    def wrapper(*args):
        result = fn(*args)
        return result.title()
    return wrapper


def run_only_between(from_, to_):
    def dec(fn):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                return fn(*args, **kwargs)
        return wrapper
    return dec


@capitalise_text
def introduce_yourself(name, age):
    return f'My name is {name} and I am {age} yo.'


@run_only_between(6, 22)
def say_something():
    return 'Hello World!'


@loving_python
def good_luck():
    return 'Good luck!'


if __name__ == "__main__":
    print(introduce_yourself('tom', 19))
    print(say_something())
    print(good_luck())

