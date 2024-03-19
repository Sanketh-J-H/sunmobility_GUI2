def extract_variables(hex_data, variables):
    # Convert hexadecimal data to integer
    hex_int = int(hex_data, 16)
    # Convert integer to binary string, remove the '0b' prefix, and pad zeros to ensure 32 bits
    binary_string = bin(hex_int)[2:].zfill(64)

    extracted_values = {}
    for variable, (start_bit, length) in variables.items():
        # Calculate the end bit position
        end_bit = start_bit + length
        # Extract bits for the current variable from the binary string (in big-endian order)
        extracted_bits = binary_string[-end_bit:-start_bit]
        # Convert the extracted bits to an integer value
        extracted_value = int(extracted_bits, 2)
        # Store the extracted value in the dictionary
        extracted_values[variable] = extracted_value

    return extracted_values

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

# Example usage:
big_endian_data = "1234567887654321"
extracted_values = extract_variables(big_endian_data, B2T_BMS1)

# Print the extracted values
for variable, value in extracted_values.items():
    print(f"{variable}: {value}")