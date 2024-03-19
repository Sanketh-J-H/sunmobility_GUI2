import socket
import time

def client(file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 1234))
        with open(file_path, 'r') as file:
            while True:
                chunk = file.readline().rstrip()
                if not chunk:
                    break
                time.sleep(0.1)
                s.sendall(bytes(chunk , encoding='utf-8'))
                # Wait for acknowledgment from server (optional)
                # ack = s.recv(1024)
                # print('Received acknowledgment from server:', ack.decode())

if __name__ == "__main__":
    file_path = "CANT_Test10Amps.log"
    client(file_path)
