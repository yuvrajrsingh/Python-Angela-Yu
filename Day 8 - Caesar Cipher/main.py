from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_number, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_amount = alphabet.index(letter) + shift_number
            shifted_amount %= len(alphabet)
            output_text += alphabet[shifted_amount]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False 
        print("Goodbye")