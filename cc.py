# Caesar Cipher Program
# This program allows the user to encrypt or decrypt messages using the Caesar Cipher algorithm.

def caesar_encrypt(text, shift):
   
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Leave non-alphabet characters unchanged
            encrypted += char
    return encrypted


def caesar_decrypt(text, shift):
    
    # Decryption is just encryption with the negative of the shift value
    return caesar_encrypt(text, -shift)


def main():
    
    print("=== Caesar Cipher Program ===")
    
    # Ask user whether to encrypt or decrypt
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("❌ Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
        return
    
    # Get the message from the user
    message = input("Enter your message: ")
    
    # Get and validate the shift value
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("❌ Shift must be an integer.")
        return
    
    # Perform the chosen operation
    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print(f"🔐 Encrypted message: {result}")
    else:
        result = caesar_decrypt(message, shift)
        print(f"🔓 Decrypted message: {result}")


# Entry point for the program
if __name__ == "__main__":
    main()
