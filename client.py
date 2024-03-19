import socket
import time

def client(file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(('127.0.0.1', 1234))

        while True:
            with open(file_path, 'rb') as file:
                for chunk in file:
                    chunk = file.readline().rstrip()
                    time.sleep(0.1)
                    s.sendall(chunk)
            
if __name__ == "__main__":
    file_path = "CANT_Test10Amps.log"
    client(file_path)
