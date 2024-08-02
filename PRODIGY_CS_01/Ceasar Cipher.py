def caesar_cipher(text, shift, mode = 'encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char.upper())
            num = ascii_val - 65
            if mode == 'encrypt':
                shifted = (num + shift) % 26
            else:
                shifted = (num - shift) % 26
            result = result + chr(shifted + 65)
        else:
            result = result + char
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        mode = input("Would you like to (e)ncrypt, (d)ecrypt, or (q)uit? ").lower()
        if mode == 'q':
            print("Thank you for using the Caesar Cipher Program!")
            break
        elif mode in ['e', 'd']:
            message = input("Enter your message: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (0-25): "))
                    if 0 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 0 and 25!")
                except ValueError:
                    print("Please enter a valid integer!")
                    
            result = caesar_cipher(message, shift, 'encrypt' if mode == 'e' else 'decrypt')
            print(f"{'Encrypted' if mode == 'e' else 'Decrypted'} message: {result}\n" )
        else:
            print("Invalid option! Please choose 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()