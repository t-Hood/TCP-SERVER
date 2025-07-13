import socket
import threading

IP = "0.0.0.0"
PORT = 9998


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP,
            PORT))
    s.listen(5)
    print(f"[*] Listening to {IP}:{PORT}")
    while True:
        conn, address = s.accept()
        print(f"[*] Got connection from: {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client,
                                          args=(conn,))
        client_handler.start()
def handle_client(client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print(f"[*] Received: {request.decode('utf-8')}")
            sock.send(b"Hello")
if __name__ == "__main__":
    main()

