""""

Basicamente o que a gente ta fazendo é usando os parâmetros
de inicialização que o terminal nos permite usar para inicializar
o programa de formas variadas, através do Argument Parsing

"""

# Exemplos de argumentos:
# python3 myscript.py result.txt -o test.txt -l DEBUG -c

def myfunc(*args, **kwargs):
    print("-"*26, "ARGS", "-"*26)
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print("-"*25, "KWARGS", "-"*25)
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myfunc('hey', True,  19, 'wow', KEYONE="TEST", KEYTWO=7)

# Da erro de "Index out of range" caso não tenha argumentos o suficiente para printar
# Ou no caso do kwargs da KeyError