def capitalise_text(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)

        return result.title()
    return wrapper


@capitalise_text
def introduce_yourself(name, age):
    return f'My name is {name} and I am {age} yo.'


if __name__ == "__main__":
    print(introduce_yourself('tom', 19))


