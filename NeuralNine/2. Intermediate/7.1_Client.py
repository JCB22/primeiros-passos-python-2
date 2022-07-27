import socket

# Inicia este programa enquanto o 7.0 estiver iniciando
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 55555))  # s.bind((address))
    # OBS: A forma em que o address é informado
    # depende da família do soquete
    message = s.recv(1024)
    s.close()

    print(message.decode())
