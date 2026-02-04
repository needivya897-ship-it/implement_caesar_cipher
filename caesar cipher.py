def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        # Encrypt / Decrypt only alphabets
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


# User Input
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()

# Output
if choice in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice! Please type encrypt or decrypt.")
