def little_to_big_endian(hex_string):
    # Split the hexadecimal string into pairs of two characters
    pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    # Reverse the order of the pairs
    pairs.reverse()
    # Join the pairs back together to form the big-endian hexadecimal string
    big_endian_hex = ''.join(pairs)
    return big_endian_hex

# Example usage:
little_endian_data = "0x21436587"
big_endian_data = little_to_big_endian(little_endian_data.replace(" ", ""))
print("Big-Endian Data:", big_endian_data)
