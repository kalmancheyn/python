

def caesar_encryption(msg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    privare_key = 19
    encry_message = ""
    for c in msg:
        position = alphabet.find(c)
        new_position = (position + privare_key) % len(alphabet)
        new_character = alphabet[new_position]
        encry_message += new_character
    return encry_message


def caesar_decryption(msg, public_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 23
    decry_message = ""
    key = int(public_key / private_key)
    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character
    return decry_message


def caesar_decipher(msg, public_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    private_key = 23
    decry_message = ""
    key = int(public_key / private_key)
    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character
    return decry_message


def main():
    s = input("Please enter message: ")
    s = caesar_encryption(s)
    print("Encrypted message: " + s)
    s = caesar_decryption(s, 19*23)
    print("Decrypted message: " + s)


if __name__=="__main__":
    main()