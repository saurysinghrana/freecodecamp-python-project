from encryption import encrypt
from decryption import decrypt

print("=== Vigenere Cipher Program ===")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option: ")

message = input("Enter your message: ")
key = input("Enter the key: ")

if choice == '1':
    result = encrypt(message, key)
    print(f"\nEncrypted text: {result}")

elif choice == '2':
    result = decrypt(message, key)
    print(f"\nDecrypted text: {result}")

else:
    print("Invalid choice.")