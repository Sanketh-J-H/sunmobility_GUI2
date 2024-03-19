import socket

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 1234))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(14)
                if not data:
                    break
                print('Received:', data)
                # Process received data here
                # For demonstration, let's send the same data back
                # conn.sendall(data)

if __name__ == "__main__":
    server()
