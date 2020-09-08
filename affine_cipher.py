# Dictionary
dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

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
    msg = input("Enter Message: ").upper()
    msg = remove(msg)
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
    
    choice = int(input("1. Encrypttion\n2. Decryption\nChoose(1,2): "))
    
    if choice == 1:
        print("--Encryption--")
        encrypted_text = affine_encrypt(msg, keycode[0], keycode[1]) 
        print('Encrypted Text: {}'.format( encrypted_text ).lower()) 

    elif choice == 2:
        print("--Decryption--")
        decrypted_text = affine_decrypt(msg, keycode[0], keycode[1])
        print('Decrypted Text: {}'.format( decrypted_text).lower())
    else:
        print("Invalid input")

main()
