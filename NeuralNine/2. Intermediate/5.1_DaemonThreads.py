import threading
import time


if __name__ == '__main__':
    path = "text.txt"
    text = ""

    def lerArquivo():
        global path, text
        while True:
            with open(path,'r') as f:
                text = f.read()
            time.sleep(3)

    def printLoop():
        for x in range(30):
            print(text)
            time.sleep(1)

    t1 = threading.Thread(target=lerArquivo, daemon=True)
    t2 = threading.Thread(target=printLoop)
