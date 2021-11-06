from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    word = 'nope10'
    key = 5
    actual = encrypt(word, 5)
    expected = 'stuj65'
    assert actual == expected


def test_decrypt():
    word = 'stuj65'
    key = 5
    actual = decrypt(word, 5)
    expected = 'nope10'
    assert actual == expected


def test_crack():
    word = 'stuj65'
    actual = crack(word)
    expected = 'nope10'
    assert actual == expected


def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected

def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected    

def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected

def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected    

def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected        

def test_decrypt_with_whitespace():
    actual = decrypt("bqqmft boe cbobobt", 1)
    expected = "apples and bananas"
    assert actual == expected     

def test_decrypt_uppercase():
    actual = decrypt("LKXKXK", 10)
    expected = "BANANA"
    assert actual == expected  
