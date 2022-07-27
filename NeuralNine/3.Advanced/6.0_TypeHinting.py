# Perceba que pelo fato do python ser
# dinamicamente tipado, Não tem como
# forçar uma variavel que a função
# receba somente int nem que retorne somente str
def myfunc(myparameter: int) -> str:
    print(myparameter)
    return 12

def otherfunc(otherparamether: str):
    print(otherparamether)

# Mas caso queira que seja estaticamente tipado
# Como no Java, pode-se usar o mypy que faz o trabalho
# De analisar as hints e ver se a tipagem está de acordo

myfunc("Hello World")
otherfunc(myfunc(23))
