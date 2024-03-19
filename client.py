import socket
import time

def client(file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 1234))
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(14)
                if not chunk:
                    break
                time.sleep(0.5)
                s.sendall(chunk)
                # Wait for acknowledgment from server (optional)
                # ack = s.recv(1024)
                # print('Received acknowledgment from server:', ack.decode())

if __name__ == "__main__":
    file_path = "CANT_Test10Amps.log"
    client(file_path)
