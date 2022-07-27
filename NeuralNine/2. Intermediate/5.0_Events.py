import threading


if __name__ == "__main__":
    event = threading.Event()


    def myFunc():
        print("Esperando evento ocorrer")
        event.wait()
        print("Performando evento")

    t1 = threading.Thread(target=myFunc)
    t1.start()

    x = input("Quer que o evento ocorra? (s/n)\n")

    if x == 's':
        event.set()
