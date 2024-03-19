import socket

# Specify the file path
file_path = "CANT_Test10Amps.log"


def send_data_to_loopback(file_path):
    
   
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to a local socket (use a different port number)
    # Connect to port 8001 on the loopback address
    s.connect(('127.0.0.1', 1234))

    # Read data from the file in chunks
    while True:
        chunk = 0
        with open(file_path, 'r') as file:
            chunk = file.read(13)  # Read 13 bytes from the file
            # file.close()

        # Convert the chunk to hex format
        # hex_data = chunk.hex()

        # Send the hex data over the connection
        s.sendall(chunk.encode())


if __name__ == "__main__":
    send_data_to_loopback(file_path)
