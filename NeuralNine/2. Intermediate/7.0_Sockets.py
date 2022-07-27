import socket

# Inicia este programa e depois o 7.1 para receber a mensagem
if __name__ == '__main__':
    # socket(Address Family, Socket Type, Protocolo)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 55555))  # s.bind((address))
    # OBS: A forma em que o address é informado
    # depende da família do soquete
    s.listen()

    while True:
        client, adress = s.accept()
        print(f"Connected to {adress}")
        client.send("You are connected!".encode())
        client.close()
