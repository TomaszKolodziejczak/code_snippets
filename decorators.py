from functools import wraps


def capitalize_text(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result.title()

    return wrapper


def as_bold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


@capitalize_text
def greeting(name: str) -> str:
    return f"hello {name}"


@capitalize_text
@as_bold
def introduce(name: str, age: int) -> str:
    return f"hello I'm {name} and I'm {age} years old"


if __name__ == "__main__":
    greetings = greeting("tOm")
    introducing = introduce("jUdy", 25)
    print(greetings)
    print(introducing)
