import string

def remove(string): 
    return string.replace(" ", "")

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
ciphertext = ''

for index in sorted(order.keys()):
   for part in split_len(plaintext, len(key)):
      try:ciphertext += part[order[index]]
         except IndexError:
            continue
   return ciphertext


def vigenere_encryption(plaintext, key):
    cipher = ""
    index = 0
    for c in plaintext:
        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')

            encrypted_c = chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
            cipher = cipher + encrypted_c

            index = (index + 1)% len(key)
        else:
            cipher = cipher + c

    return cipher

def vigenere_decryption(cipher, key):
    plaintext = ""
    index = 0
    for c in cipher:

        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')
            decrypted_c_num = ord(c) - ord('a') - offset
            if decrypted_c_num < 0:
                decrypted_c_num = decrypted_c_num + 26

            decrypted_c = chr(decrypted_c_num + ord('a'))

            plaintext = plaintext + decrypted_c
            index = (index + 1) % len(key)

        else:
            plaintext = plaintext + c
    
    return plaintext
        
def main():
    
    message = input("Enter Message: ").lower()
    message = remove(message)
    keycode = input("Enter Key: ").lower()
    transpose_key = input("Enter Transpose Key: ")
    
    choice = int(input("1. Encrypttion\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("--Encryption--")
        enc_message =  vigenere_encryption(message, keycode)
        enc_message = 
        print(enc_message)

    elif choice == 2:
        print("--Decryption--")
        message = vigenere_decryption(message, keycode)
        print(message)

    else:
        print("Invalid Input")

main()
