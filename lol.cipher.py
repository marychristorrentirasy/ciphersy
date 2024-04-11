def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            elif char.islower():
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

# Example usage:
plaintext = "Hello, classmates!"
shift = 3
encrypted_message = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted Message:", encrypted_message)

decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)


print(''Mary Chris T, Sy'')
print("IT36-A")
print("IAS")