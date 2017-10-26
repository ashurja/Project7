# Jamshed Ashurov
# 08/26/17
# cipher.py
# This program creates a program that can encode or decode the words

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode():
    """
    This function asks the user to input the word he wants to encode and the rotation key in order to encode the words
    :return:
    """
    encode_word = input("What word to do you want to encode?")
    rotation_number = int(input("Please enter the rotation key: "))
    word = []
    lower_key = encode_word.lower()
    if " " in lower_key:
        lower_key = lower_key.replace(" ", "")
    for x in lower_key:
        position = alphabet.index(x)
        new_letter = alphabet[(rotation_number + position) % 26]
        word.append(new_letter)
    new_word = "".join(word)
    print(new_word)


def decode():
    """
    This function asks the user to input the word he wants to decode and the rotation key in order to show the original
    text
    secure
    :return:
    """
    decode_word = input("What word to do you want to decode?")
    rotation_number = int(input("Please enter the rotation key: "))
    word = []
    lower_key = decode_word.lower()
    if " " in lower_key:
        lower_key = lower_key.replace(" ", "")
    for x in lower_key:
        position = alphabet.index(x)
        new_letter = alphabet[(position - rotation_number) % 26]
        word.append(new_letter)
    new_word = "".join(word)
    print(new_word)


def main():
    game = input("Press e to encode, d to decode, and q to quit:")
    while game != "q":
        if game == "e":
            encode()
        elif game == "d":
            decode()
        game = input("Press e to encode, d to decode, and q to quit:")
    print("Oh well, next time then")

main()
