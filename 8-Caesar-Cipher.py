import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(plain_text, shift_amount, the_direction):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if the_direction == "encode":
        new_position = position + shift_amount
    else:
        new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")
  
rep_loop = False
while rep_loop == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, the_direction=direction)
    again = input("Do you want to go again? Yes or No? ").lower()
    if again == "no":
        rep_loop = True
