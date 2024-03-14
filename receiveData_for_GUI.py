import socket
import os
import threading

# B2T_BMS1 = {}
# keys = [
#     "B2T_BMS1_Message_sum",
#     "B2T_TMax",
#     "B2T_Tmin",
#     "B2T_ScBatU_H",
#     "B2T_ScBatU_L",
#     "B2T_Mode",
#     "B2T_TMSWorkMode",
#     "B2T_BMUWorkMode",
#     "B2T_HighVCtrl",
#     "B2T_TargetT",
#     "B2T_TAvg",
#     "B2T_Life"
# ]

# Define variables and their start bits and lengths
B2T_BMS1 = {
    "B2T_TMax": (0, 8),
    "B2T_Tmin": (8, 8),
    "B2T_ScBatU_H": (16, 8),
    "B2T_ScBatU_L": (24, 8),
    "B2T_Mode": (32, 1),
    "B2T_TMSWorkMode": (33, 3),
    "B2T_BMUWorkMode": (36, 1),
    "B2T_HighVCtrl": (39, 1),
    "B2T_TargetT": (40, 8),
    "B2T_TAvg": (48, 8),
    "B2T_Life": (56, 8)
}
# B2T_BMS1 = {
#     "B2T_TMax": (56, 8),
#     "B2T_Tmin": (48, 8),
#     "B2T_ScBatU_H": (40, 8),
#     "B2T_ScBatU_L": (32, 8),
#     "B2T_Mode": (31, 1),
#     "B2T_TMSWorkMode": (28, 1),
#     "B2T_BMUWorkMode": (25, 3),
#     "B2T_HighVCtrl": (24, 1),
#     "B2T_TargetT": (16, 8),
#     "B2T_TAvg": (8, 8),
#     "B2T_Life": (0, 8)
# }


class B2TServer:
    def __init__(self):

        self.network_BSSID = 'F0:C8:14:77:98:9D'
        # self.network_BSSID = '60:FB:00:2E:A0:BF'
        # self.network_BSSID = '60:FB:00:2E:A0:BA'
        self.password = '12345678'
        self.SERVER_IP = '192.168.1.12'
        self.SERVER_PORT = 8001
        self.index = 0

    def create_socket(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.SERVER_IP, self.SERVER_PORT))
        self.lock = threading.Lock()  # Add a lock for thread safety

    def connect_to_wifi(self):
        command = f"nmcli device wifi connect {self.network_BSSID} password {self.password}"
        exit_code = os.system(command)
        if exit_code == 0:
            print(
                f"Successfully connected to WiFi network: {self.network_BSSID}")
        else:
            print(
                f"Error: Failed to connect to WiFi network {self.network_BSSID}")

    def disconnect_from_wifi(self):
        command = f"nmcli device disconnect wlp4s0"
        exit_code = os.system(command)
        if exit_code == 0:
            print(f"Device 'wlp4s0' successfully disconnected.")
        else:
            print(f"Error: Failed to disconnect from Device 'wlp4s0'.")

    def receive_data_from_socket(self):
        data, _ = self.server_socket.recvfrom(13)
        hex_data = data.hex()  # Convert received data to Hexadecimal
        return hex_data

    def get_B2T_BMS1(self):
        global B2T_BMS1
        # with self.lock
        return B2T_BMS1.copy()  # Return a copy to avoid directly exposing the internal dictionary

    def start_server(self):
        global B2T_BMS1
        global keys
        self.disconnect_from_wifi()
        self.connect_to_wifi()
        self.create_socket()
        print("UDP server is listening...")
        while True:
            received_data = self.receive_data_from_socket()
            print(received_data)

            # Check if the received data starts with the desired prefix
            if str(received_data[2:]).startswith('18ff45f3'):
                # Extract the relevant portion of the received data (after the prefix)
                # Mask out all but the last 64 bits
                trimmed_data = int(received_data, 16) & 0xffffffffffffffff
                # trimmed_data = hex(trimmed_data)
                # Convert hex data to binary string
                binary_data = bin(trimmed_data)[2:].zfill(64)
                # # Assign the extracted data to the corresponding key in the dictionary
                # B2T_BMS1[keys[self.index]] = trimmed_data
                # # Increment the index for the next key
                # self.index = (self.index + 1) % len(keys)
                # Decrypt hex data into separate variables
                decrypted_data = {}
                for var, (start_bit, length) in B2T_BMS1.items():
                    end_bit = start_bit + length
                    value = int(binary_data[start_bit:end_bit], 2)
                    decrypted_data[var] = value
                print(decrypted_data)

                # Define the output string
                output_string = f' {decrypted_data}'
    
                # Specify the file path
                file_path = "CANT_Test.log"
    
                # Write the output string to the file
                with open(file_path, "w") as file:
                    file.write(output_string)

    def stop_server(self):
        self.server_socket.close()


if __name__ == "__main__":
    server = B2TServer()
    server_thread = threading.Thread(target=server.start_server)
    # server_thread.daemon = True  # Run the thread as a daemon so it exits when the main program exits
    server_thread.start()
    # Other GUI-related code can go here
