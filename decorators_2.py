def loving_python(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print('No matter what the function returns, let everyone know You love Python!')
        return result
    return wrapper


def capitalise_text(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)

        return result.title()
    return wrapper


@loving_python
@capitalise_text
def introduce_yourself(name, age=0):
    return f'My name is {name} and I am {age} yo.'


if __name__ == "__main__":
    print(introduce_yourself('tom', 19))


