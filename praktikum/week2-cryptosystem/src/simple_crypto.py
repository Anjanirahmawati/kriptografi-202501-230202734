# file: praktikum/week2-cryptosystem/src/simple_crypto_with_digits.py

def encrypt(plaintext, key):
    """
    Encrypt plaintext:
    - letters: rotated within A-Z or a-z (26)
    - digits: rotated within 0-9 (10)
    - other chars: unchanged
    """
    result = []
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift + key) % 26 + shift))
        elif char.isdigit():
            result.append(chr((ord(char) - 48 + key) % 10 + 48))
        else:
            result.append(char)
    return "".join(result)


def decrypt(ciphertext, key):
    """
    Decrypt ciphertext using inverse rotation.
    """
    result = []
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift - key) % 26 + shift))
        elif char.isdigit():
            result.append(chr((ord(char) - 48 - key) % 10 + 48))
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    message = "<230202734><anjani rahmawati>"
    key = 5  

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
