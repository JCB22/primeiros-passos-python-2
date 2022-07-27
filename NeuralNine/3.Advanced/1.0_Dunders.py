"""

Dunder(Double Underscore

Exemplo: "__init__" é ativado quando um objeto é inicializado

"""
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __del__(self):
        print(f"{self.name} sendo eliminado!")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sem essa função, v1+v2 vai dar erro
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Sem essa função, o v3 vira "<__main__.Vector object at 0x0000024D385B2D90>"
    # Usar __repr__ também daria no mesmo
    def __str__(self):
        return f"X: {self.x}\t Y: {self.y}"

    # O que acontece se você chamar o vetor?
    # "v3()"
    def __call__(self, *args, **kwargs):
        print("Eu fui chamado!")

if __name__ == '__main__':
    p1 = Person('Mike', 150)

    v1 = Vector(10,30)
    v2 = Vector(20, 60)
    v3 = v1 + v2

    print(v3)

    v3()
