def encrypt_decrypt(message, key):
    result = ''
    for letter in message:
        result += chr(ord(letter) ^ key)
    return result


if __name__ == '__main__':
    text = "Hello World"
    enc_key = 20500
    encrypted = encrypt_decrypt(text, enc_key)
    print(encrypted)
    decrypted = encrypt_decrypt(encrypted, enc_key)
    print(decrypted)
