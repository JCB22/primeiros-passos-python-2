import threading
import time


if __name__ == '__main__':
    x = 8192


    def double():
        global x, lock
        lock.acquire()
        while x < 16384:
            x *= 2
            print(x)
            time.sleep(1)
        print("Maximo valor!")
        lock.release()


    def halve():
        global x, lock
        lock.acquire()
        while x > 1:
            x /= 2
            print(x)
            time.sleep(1)
        print("Valor Mínimo!")
        lock.release()

    lock = threading.Lock()

    t1 = threading.Thread(target=halve)
    t2 = threading.Thread(target=double)

    t1.start()
    t2.start()
    # As duas threads nunca vao parar de dobrar/dividir
    # A não ser que a gente usa o Locking
