import string

message = ""
keycode = ""
enc_message = ""

def remove(string): 
    return string.replace(" ", "")

   
def vigenere_encryption(plaintext, key):
    cipher = ""
    index = 0
    for c in plaintext:
        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')

            encrypted_c = chr((ord(c) - ord('a') + offset) % 256 + ord('a')) 
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
                decrypted_c_num = decrypted_c_num + 256

            decrypted_c = chr(decrypted_c_num + ord('a'))

            plaintext = plaintext + decrypted_c
            index = (index + 1) % len(key)

        else:
            plaintext = plaintext + c
    
    return plaintext
        
def main():
    mode = int(input("1. Type Text\n2. Input File\nChoose(1,2): "))
    if mode == 1:
            
        message = input("Enter Message: ")
        message = remove(message)
        keycode = input("Enter Key: ")
        
        choice = int(input("1. Encrypttion\n2. Decryption\nChoose(1,2): "))
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                print(enc_message)
            elif space == 2:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = " ".join(enc_message[i:i + 5] for i in range(0, len(enc_message), 5))
                print(enc_message)
            else:
                print("Invalid Input")

        elif choice == 2:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                message = vigenere_decryption(message, keycode)
                print(message)
            elif space == 2:
                print("--Decryption--")
                message = vigenere_decryption(message, keycode)
                message = " ".join(message[i:i + 5] for i in range(0, len(message), 5))
                print(message)
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")

    elif mode == 2:

        infile_name = input("Enter input file name: ")
        infile = open(infile_name, 'r+')

        message = infile.read()
        message = remove(message)
        keycode = input("Enter Key: ")
        
        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                print(enc_message)

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(enc_message)
                else:
                    pass
                    
            elif space == 2:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = " ".join(enc_message[i:i + 5] for i in range(0, len(enc_message), 5))
                print(enc_message)

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(enc_message)
                else:
                    pass
            else:
                print("Invalid Input")
            

        elif choice == 2:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                message = vigenere_decryption(message, keycode)
                print(message)
            elif space == 2:
                print("--Decryption--")
                message = vigenere_decryption(message, keycode)
                message = " ".join(message[i:i + 5] for i in range(0, len(message), 5))
                print(message)
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid input")
        

main()
