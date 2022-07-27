

def mydecorator(function):

    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function!")

        return return_value

    return wrapper


"""
    A função wrapper recebe uma função e seus parâmetros
    e é ideal que a função seja capaz de receber qualquer
    informação e poder executar a função dada, por isso a expressão
    *arg,**kwargs (argumentos, argumentos "palavra-chave") será usada
    para tornar universal a função
"""


# @mydecorator
# def helloWorld():
#     print("Hello World!")

# helloWorld()

def hello(person):
    print(f'Hello, {person}')
    return f"Hello, {person}! How was your day?"


#hello("Gustavo")
print(hello("Gustavo"))
