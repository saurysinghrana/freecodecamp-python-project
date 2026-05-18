from cipher_utils import alphabet

def decrypt(message, key):
    final_message = ''
    key_index = 0

    for char in message.lower():

        # Keep spaces and special characters unchanged
        if not char.isalpha():
            final_message += char

        else:
            # Get key character
            key_char = key[key_index % len(key)]
            key_index += 1

            # Decrypt character
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)

            final_message += alphabet[new_index]

    return final_message