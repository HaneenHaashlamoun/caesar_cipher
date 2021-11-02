import re
import nltk
from nltk.corpus import words, names
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()


def encrypt(plain_text, shifted):
    encrypted = ""
    for char in plain_text:
        if char.isupper():
            char_index = ord(char) - ord('A')
            shifted_i = (char_index + shifted) % 26 + ord('A')
            encrypted_char = chr(shifted_i)
            encrypted += encrypted_char
        elif char.islower():
            char_index = ord(char) - ord('a')
            shifted_i = (char_index + shifted) % 26 + ord('a')
            encrypted_char = chr(shifted_i)
            encrypted += encrypted_char
        elif char.isdigit():
            number = (int(char) + shifted) % 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted


def decrypt(encrypted, shifted):
    decrypted = ""
    for char in encrypted:
        if char.isupper():
            char_index = ord(char) - ord('A')
            shifted_i = (char_index - shifted) % 26 + ord('A')
            decrypted_char = chr(shifted_i)
            decrypted += decrypted_char
        elif char.islower():
            char_index = ord(char) - ord('a')
            shifted_i = (char_index - shifted) % 26 + ord('a')
            decrypted_char = chr(shifted_i)
            decrypted += decrypted_char
        elif char.isdigit():
            decrypted_number = (int(char) - shifted) % 10
            decrypted += str(decrypted_number)
        else:
            decrypted += char
    return decrypted

def crack(encrypted):
    for i in range(26):
        decrypted =  decrypt(encrypted,i)
        word = re.sub(r'[^A-Za-z]+','', decrypted)
        if word.lower() in word_list or word in name_list:
            return (decrypted)
