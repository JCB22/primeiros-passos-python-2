import abc
from abc import ABCMeta

class IPerson(metaclass=ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def print_data():
        """ Implement child class """

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instanciated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f'Name: {PersonSingleton.__instance.name}\nAge: {PersonSingleton.__instance.age}')


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()

# p2 = PersonSingleton("John", 25)
"""
Esta linha de código vai causar um raise Exception porque decidimos
que não deverá ter mais de uma pessoa no nosso programa.
Pensa como aqueles servidores que não deve ter mais de um mapa, por exemplo
"""
