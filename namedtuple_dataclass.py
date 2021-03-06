from collections import namedtuple
from dataclasses import dataclass, field
from typing import List


my_data = [
    {
        "name": "John",
        "Surname": "Johnson"
    },
    {
        "name": "Arthur",
        "Surname": "Dwight",
    }
]

Person = namedtuple('Person', 'name surname')


def labeled_entries(data: List) -> List[Person]:
    return [Person([entry['name']], Person[entry['surname']]) for entry in data]


@dataclass()
class Student:
    name: str
    surname: str
    age: int
    grades: List = field(default_factory=list)

    def add_grades(self, *grades):
        for grade in grades:
            if 1 <= grade <= 6:
                self.grades.append(grade)
            else:
                raise ValueError(f"Grade {grade} is out of range 1-6")

    def remove_grade(self, idx: int):
        try:
            return self.grades.pop(idx)
        except IndexError:
            raise IndexError("Can't delete index - out of range")


@dataclass(order=True)
class Country:
    name: str = field(compare=False)
    population: int
    area: float
    coastline: float

    
my_countries = [
    Country('Hungary', 4000, 5000.24, 700.5),
    Country('Germany', 3000, 5000.24, 800.5),
    Country('Poland', 5000, 5000.24, 900.5),
]

print(sorted(my_countries, key=lambda x: x.population))




