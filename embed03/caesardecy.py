def caesar_decryption(msg, public_key, private_key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decry_message = ""
    key = int(public_key / private_key)

    for c in msg:
        position = alphabet.find(c)
        new_position = (position - key) % len(alphabet)
        new_character = alphabet[new_position]
        decry_message += new_character
    return decry_message


if __name__ == '__main__':
    public_keys = [10, 77, 221, 437]
    encrypted = "iqfihhih"

    private_keys = [2, 7, 13, 19]

    for b in public_keys:
        public_key = b
        for d in private_keys:
            private_key = d
            decry_message = caesar_decryption(encrypted, public_key, private_key)
            print("private key:", private_key, "public key:", public_key, "word:", decry_message)


