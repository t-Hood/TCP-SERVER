import socket

target_host = "127.0.0.1"
target_port = 9998


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target_host, target_port))
        while True:
            inputss = input("Type something: ")
            s.send(inputss.encode('utf-8'))
            response = s.recv(1024)
            print(response.decode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()
    input("Press enter to quit")
