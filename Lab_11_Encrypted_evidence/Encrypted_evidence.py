import string
from base64 import b64decode
 
file_path = 'intercepted.txt'
with open(file_path, 'r') as file:
    intercepted_text = file.read().strip()
 
def decrypt_step1(s):
    translation_table = str.maketrans(
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    )
    decrypted = str.translate(s, translation_table)
    print('Decrypted text after Step 1:', decrypted)
    return decrypted
 
def decrypt_step2(s):
    """
    Decrypt using Step 2 logic: Reverse Base64 encoding.
    """
    try:
        decoded = b64decode(s.encode())
        decrypted = decoded.decode('utf-8')  # Convert bytes to string
    except UnicodeDecodeError:
        decrypted = b64decode(s).decode('latin-1')
    print('Decrypted text after Step 2:', decrypted)
    return decrypted
 
def decrypt_step3(ciphertext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]  
    translation_table = str.maketrans(shifted_string, loweralpha)
    decrypted = str.translate(ciphertext, translation_table)
    print('Decrypted text after Step 3:', decrypted)
    return decrypted
 
# Print the intercepted ciphertext
print('Intercepted Ciphertext:', intercepted_text)
 
# Sequence to track the order of decryption steps
decryption_steps_sequence = []
 
# Partial decrypted text
partial_decrypted_text = intercepted_text
 
# Process the ciphertext while its first character is numeric (indicating a step)
while partial_decrypted_text[:1].isnumeric():
    current_step = partial_decrypted_text[:1]
    print('Applying decryption step:', current_step)
 
    decryption_steps_sequence.append(current_step)
 
    partial_decrypted_text = partial_decrypted_text[1:]
    if current_step == '2':  # Step 2 (Base64) might require padding
        partial_decrypted_text += '='
 
    decryption_function = globals()[f'decrypt_step{current_step}']
    partial_decrypted_text = decryption_function(partial_decrypted_text)
 
    print('Partial decrypted text:', partial_decrypted_text)
 
# Print the final plaintext
print('Plaintext (i.e., Secret Message):', partial_decrypted_text)
print('Decryption steps sequence:', decryption_steps_sequence)
 
