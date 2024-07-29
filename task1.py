


def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift * mode) % 26 + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted message:", caesar_cipher(text, shift, 1))
        elif choice == "2":
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted message:", caesar_cipher(text, shift, -1))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
