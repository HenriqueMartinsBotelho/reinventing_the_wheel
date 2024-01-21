import socket

# Configurações do servidor
HOST = '127.0.0.1'  # O servidor está rodando no localhost
PORT = 1234         # A porta usada pelo servidor

# Cria um socket IPv4 (AF_INET) do tipo SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server.")

    message = "Hello, Server!"
    s.sendall(message.encode('utf-8'))
    print(f"Sent: {message}")

    data = s.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    # s.sendall(b'q')
    # print("Sent 'q' to close the connection.")

    # data = s.recv(1024)
    # print(f"Final received (if any): {data.decode('utf-8')}")
