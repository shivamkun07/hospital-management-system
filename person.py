from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    @abstractmethod
    def display_details(self):
        pass