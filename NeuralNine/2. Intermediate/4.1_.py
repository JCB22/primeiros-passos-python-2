import threading
import time

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print(f"{thread_number} esta tentando acessar!")
    semaphore.acquire()
    print(f"O acesso de {thread_number} foi garantido!")
    time.sleep(10)
    print(f"{thread_number} está fazendo o release!")
    semaphore.release()


for thread_number in range(1, 10):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
