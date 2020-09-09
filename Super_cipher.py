# Python3 implementation of 
# Columnar Transposition 
import math
import string

def remove(string): 
    return string.replace(" ", "")

   
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

# Encryption 
def trans_encrypt(msg, key): 
    cipher = "" 

    # track key indices 
    k_indx = 0

    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 

    # calculate column of the matrix 
    col = len(key) 
    
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 

    # add the padding character '_' in empty 
    # the empty cell of the matix 
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 

    # create Matrix and insert message and 
    # padding characters row-wise 
    matrix = [msg_lst[i: i + col] 
        for i in range(0, len(msg_lst), col)]
    print(matrix)

    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx] 
            for row in matrix]) 
        k_indx += 1

    return cipher

# Decryption 
def trans_decrypt(cipher, key): 
    msg = "" 

    # track key indices 
    k_indx = 0

    # track msg indices 
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 

    # calculate column of the matrix 
    col = len(key) 
    
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 

    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position. 
    key_lst = sorted(list(key)) 

    # create an empty matrix to 
    # store deciphered message 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 

    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 

        for j in range(row): 
                dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
                msg_indx += 1
        k_indx += 1

    # convert decrypted msg matrix into a string 
    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot, handle repeating words.") 

    null_count = msg.count('_') 

    if null_count > 0: 
        return msg[: -null_count] 

    return msg



def main():
    mode = int(input("1. Type Text\n2. Input File\nChoose(1,2): "))
    if mode == 1:
            
        message = input("Enter Message: ").lower()
        message = remove(message)
        keycode = input("Enter Key: ").lower()
        
        choice = int(input("1. Encrypttion\n2. Decryption\nChoose(1,2): "))
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = trans_encrypt(enc_message,keycode)
                print(enc_message)
            elif space == 2:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = trans_encrypt(enc_message,keycode)
                enc_message = " ".join(enc_message[i:i + 5] for i in range(0, len(enc_message), 5))
                print(enc_message)
            else:
                print("Invalid Input")

        elif choice == 2:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                message = (trans_decrypt(message,keycode))
                message = vigenere_decryption(message, keycode)
                print(message)
            elif space == 2:
                print("--Decryption--")
                message = (trans_decrypt(message,keycode))
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
        message = remove(message).lower()
        keycode = input("Enter Key: ").lower()
        
        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = trans_encrypt(enc_message,keycode)
                print(enc_message)

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(enc_message)
                else:
                    pass
                    
            elif space == 2:
                print("--Encryption--")
                enc_message = vigenere_encryption(message, keycode)
                enc_message = trans_encrypt(enc_message,keycode)
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
                message = (trans_decrypt(message,keycode))
                message = vigenere_decryption(message, keycode)
                print(message)
            elif space == 2:
                print("--Decryption--")
                message = (trans_decrypt(message,keycode))
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
