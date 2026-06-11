def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - ord('A') + key) % 26 + ord('A'))
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.upper()) - ord('A') - key) % 26 + ord('A'))
        else:
            result += ch

    return result


text = input("Enter Plain Text: ")
key = int(input("Enter Key: "))

cipher = encrypt(text, key)
plain = decrypt(cipher, key)

print("Encrypted Text :", cipher)
print("Decrypted Text :", plain)