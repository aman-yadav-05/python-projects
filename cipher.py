alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for repetative ness

flag = True

while flag:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position+shift_amount
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                end_text += letter
        print(f" the {cipher_direction}d text is {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    res = input("do you want to continue? yes or no?").lower()
    if res == "no":
        flag = False
        print("Everything secured")

# #removing repetative function
# def encrypt(plain_text, amount_shift):
#     cipher_text = ""
#     for i in plain_text:
#         # we need to use list.index() function to get the index of the specific letter from the word in alphabet list
#         position = alphabet.index(i)
#         new_position = position+amount_shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"encrypted sentence is:{cipher_text}")


# def decrypt(cipher_text, amount_shift):
#     # cipher_text = ""
#     original_text = ""
#     for i in cipher_text:
#         # we need to use list.index() function to get the index of the specific letter from the word in alphabet list
#         position = alphabet.index(i)
#         new_position = position-amount_shift
#         new_letter = alphabet[new_position]
#         original_text += new_letter

#     print(f"decrypted sentence is:{original_text}")


# # encrypt(plain_text=text, amount_shift=shift)
# decrypt(cipher_text=ciph, amount_shift=shift)

# if direction == "encode":
#     encrypt(plain_text=text, amount_shift=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, amount_shift=shift)
# else:
#     print("you have entered wrong string.")
