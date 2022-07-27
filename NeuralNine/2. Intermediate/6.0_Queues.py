import queue
import time

if __name__ == "__main__":


    q = queue.Queue()
    # 1, 2, 3, 4, 5
    numbers = [10, 20, 30, 40, 50, 60, 70]
    for number in numbers:
        q.put(number)

    print(q.get())

    print("Agora comparando à versão 'Lifo Queue' ")
    time.sleep(10)

    q = queue.LifoQueue()
    numbers = [1, 2, 3, 4, 5, 6, 7]
    for x in numbers:
        q.put(x)

    print(q.get())
