"""

Recursão

Quando você pega uma função que se retorna n quantidade de vezes
exemplos práticos: Fatorial e Fibonacci

"""


def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number



if __name__ == "__main__":

    n = 7

    fact = 1

    while n > 0:
        fact *= n
        n -= 1

    print(fact)

    factorial(2)
