# Dictionary
dict1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
         'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
         'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
         'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
         'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

dict2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
         5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
         10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
         15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
         20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def remove(string): 
    return string.replace(" ", "")

#C = (a*P + b) % 26
def affine_encrypt(msg, a, b):
    cipher = ''
    for letter in msg:
        if letter == ' ':
            cipher += ' '
        else:
            z = (a*dict1[letter] + b) % 26
            cipher += dict2[z]

    return cipher


#P = (a^-1 * (C - b)) % 26
def affine_decrypt(cipher, a, b):
    message = ''
    a_inv = 0
    flag = 0
    for i in range(26):
        flag = (a*i) % 26
        if flag == 1:
            a_inv = i
            break

    for letter in cipher:
        if letter == ' ':
            message += ' '
        else:
            z = (a_inv*(dict1[letter]-b)) % 26
            message += dict2[z]

    return message


def main(): 
    mode = int(input("1. Type Text\n2. Input File\nChoose(1,2): "))
    if mode == 1:
        msg = input("Enter Message: ")
        msg = remove(msg).lower()
        keycode = []

        for i in range(0, 2):
            if (i == 0):
                print("Enter a key")
            else:
                print("Enter b key")
            ele = int(input()) 
      
            keycode.append(ele)
            if (i == 0):
                print()
              
        print(keycode)
        
        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                encrypted_text = affine_encrypt(msg, keycode[0], keycode[1]) 
                print('Encrypted Text: {}'.format( encrypted_text ).lower()) 
            elif space == 2:
                print("--Encryption--")
                encrypted_text = affine_encrypt(msg, keycode[0], keycode[1])
                encrypted_text = " ".join(encrypted_text[i:i + 5] for i in range(0, len(encrypted_text), 5))
                print('Encrypted Text: {}'.format( encrypted_text ).lower())
            else:
                print("Invalid Input")
            

        elif choice == 2:
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                decrypted_text = affine_decrypt(msg, keycode[0], keycode[1])
                print('Decrypted Text: {}'.format( decrypted_text).lower()) 
            elif space == 2:
                print("--Decryption--")
                decrypted_text = affine_decrypt(msg, keycode[0], keycode[1])
                decrypted_text = " ".join(decrypted_text[i:i + 5] for i in range(0, len(decrypted_text), 5))
                print('Decrypted Text: {}'.format( decrypted_text).lower())
            else:
                print("Invalid Input")

            
    elif mode == 2:
        infile_name = input("Enter input file name: ")
        infile = open(infile_name, 'r+')
        msg = infile.read()

        msg = remove(msg).lower()
        keycode = []

        for i in range(0, 2):
            if (i == 0):
                print("Enter a key")
            else:
                print("Enter b key")
            ele = int(input()) 
      
            keycode.append(ele)
            if (i == 0):
                print()
              
        print(keycode)
        
        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        
        if choice == 1:
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                encrypted_text = affine_encrypt(msg, keycode[0], keycode[1]) 
                print('Encrypted Text: {}'.format( encrypted_text ).lower())

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(encrypted_text)
                else:
                    pass
                
            elif space == 2:
                print("--Encryption--")
                encrypted_text = affine_encrypt(msg, keycode[0], keycode[1])
                encrypted_text = " ".join(encrypted_text[i:i + 5] for i in range(0, len(encrypted_text), 5))
                print('Encrypted Text: {}'.format( encrypted_text ).lower())

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(encrypted_text)
                else:
                    pass
                
            else:
                print("Invalid Input") 

        elif choice == 2:
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                decrypted_text = affine_decrypt(msg, keycode[0], keycode[1])
                print('Decrypted Text: {}'.format( decrypted_text).lower()) 
            elif space == 2:
                print("--Decryption--")
                decrypted_text = affine_decrypt(msg, keycode[0], keycode[1])
                decrypted_text = " ".join(decrypted_text[i:i + 5] for i in range(0, len(decrypted_text), 5))
                print('Decrypted Text: {}'.format( decrypted_text).lower())
            else:
                print("Invalid Input")
        else:
            print("Invalid input")
    else:
        print("Invalid Input")
main()
