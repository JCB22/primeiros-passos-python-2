import threading


#def helloworld():
#    print("Hello World!")

def function1():
    for x in range(10000):
        print("ONE")

def function2():
    for x in range(10000):
        print("TWO")


if __name__ == '__main__':

    t1 = threading.Thread(target=function1)
    t1.start()

    t1.join() # Espere essa thread terinar e depois executa o resto do código

    print("Outra Mensagem")
    #t2 = threading.Thread(target=function2)
    #t2.start()
