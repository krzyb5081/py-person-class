class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if (
            person.get("wife") is None 
            and person.get("husband") is None
        ):
            continue
        elif person.get("husband", None) is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
        elif person.get("wife", None) is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
    person_list = []
    for person in Person.people.values():
        person_list.append(person)
    return person_list
