# Get ASCII value of a character
ascii_value = ord('A')  # Returns 65

# Get character from an ASCII value
character = chr(65)  # Returns 'A'

print(f"The ASCII value of 'A' is {ascii_value}")
print(f"The character for ASCII value 65 is {character}")





import base64

def convert_strings(strings):
    # Create a dictionary to store Base64 and Hex values
    base64_hex_values = {}

    for s in strings:
        # Encode string to bytes
        byte_string = s.encode('utf-8')
        
        # Convert to Base64
        base64_value = base64.b64encode(byte_string).decode('utf-8')
        
        # Convert to Hex
        hex_value = byte_string.hex()
        
        # Store results in the dictionary
        base64_hex_values[s] = {
            'Base64': base64_value,
            'Hex': hex_value
        }

    return base64_hex_values

# List of strings to convert
strings_to_convert = ["Hello", "hello", "HELLO"]
result = convert_strings(strings_to_convert)

# Print the results
for string, values in result.items():
    print(f"String: {string}\nBase64: {values['Base64']}\nHex: {values['Hex']}\n")
