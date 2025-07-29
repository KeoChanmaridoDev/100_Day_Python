import art
print (art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            cipher_text += char
        else:
           shift_position = alphabet.index(char) + shift_amount
           # Use modulo to wrap around the alphabet
           shift_position %= len(alphabet)
           cipher_text += alphabet[shift_position]
    print(f"The {encode_or_decode}d text is: {cipher_text}")

userInput = True

while userInput:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function inside the loop
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        userInput = False
        print("Goodbye!")