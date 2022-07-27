import queue

if __name__ == "__main__":
    q = queue.PriorityQueue()

    # put(priority, value)
    q.put((2, "Hello World!"))
    q.put((11, 99))
    q.put((5, 7.5))
    q.put((1, True))
    # Quanto menor o número maior a prioridade, sendo 1 o máximo

    while not q.empty():
        print(q.get())
