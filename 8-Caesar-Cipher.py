alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_list = []

def encrypt(text, shift):

    text_list = list(text)
    num = 0
    
    for i in text_list: #loops through the letters from the input and checks it against the alphabet list. if they match then that letter is added to encrypted list.
        al_num = 0
        for i in alphabet:
            if text_list[num] == alphabet[al_num]:
                if al_num + shift > 25:
                    al_num -= 25
                    encrypted_list.append(alphabet[al_num + shift - 1])
                else:
                    encrypted_list.append(alphabet[al_num + shift]) #shift changes the letters depending on what the input is. For example A becomes C if the shift is 2
            al_num += 1
        num += 1

    encrypted_word = ""

    for i in encrypted_list:
        encrypted_word += i

    print(encrypted_word)

encrypt(text, shift)