import sys
import numpy as np
import string


def remove(string):
    return string.replace(" ", "")

def hill_encryption(msg, key):

    # Jika panjang message ganjil append 0
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg to matrix
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1


    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # Mencari Determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # Mencari Invers
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()

    encryp_text = ""
    itr_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)

    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)


    return encryp_text


def hill_decryption(msg, key):
    # Jika panjang message ganjil append 0
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg to matrix
    row = 2
    col = int(len(msg) / 2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1



    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1


    # Mencari Determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # mencari invers
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # adjoin
    # Transpos matrix
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # Mengganti Tanda
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # invers dikali adjoin
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plain
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)

    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)

    return decryp_text


def main():
    mode = int(input("1. Type Text\n2. Input File\nChoose(1,2): "))
    if mode == 1:
        message = input("Enter message: ").upper()
        message = remove(message)
        keycode = input("Enter 4 letter Key String: ").upper()
        keycode = remove(keycode)

        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("---Encryption---")
                encrypted_text = hill_encryption(message, keycode)
                print("Encrypted Text: {}".format(encrypted_text).lower())
            elif space == 2:
                print("---Encryption---")
                encrypted_text = hill_encryption(message, keycode)
                encrypted_text = " ".join(encrypted_text[i:i + 5] for i in range(0, len(encrypted_text), 5))
                print("Encrypted Text: {}".format(encrypted_text).lower())
            else:
                print("Invalid Input")



        elif choice == 2:
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("---Decryption---")
                decrypted_text = hill_decryption(message, keycode)
                print("Decrypted Text: {}".format(encrypted_text).lower())
            elif space == 2:
                print("---Encryption---")
                decrypted_text = hill_decryption(message, keycode)
                decrypted_text = " ".join(decrypted_text[i:i + 5] for i in range(0, len(decrypted_text), 5))
                print("Decrypted Text: {}".format(decrypted_text).lower())
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")

    elif mode == 2:
        infile_name = input("Enter input file name: ")
        infile = open(infile_name, 'r+')

        message = infile.read()
        message = remove(message).upper()

        keycode = input("Enter 4 letter Key String: ").upper()
        keycode = remove(keycode)

        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("---Encryption---")
                encrypted_text = hill_encryption(message, keycode)
                print("Encrypted Text: {}".format(encrypted_text).lower())

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(encrypted_text)
                else:
                    pass

            elif space == 2:
                print("---Encryption---")
                encrypted_text = hill_encryption(message, keycode)
                encrypted_text = " ".join(encrypted_text[i:i + 5] for i in range(0, len(encrypted_text), 5))
                print("Encrypted Text: {}".format(encrypted_text).lower())

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
                print("---Decryption---")
                decrypted_text = hill_decryption(message, keycode)
                print("Decrypted Text: {}".format(encrypted_text).lower())
            elif space == 2:
                print("---Decryption---")
                decrypted_text = hill_decryption(message, keycode)
                decrypted_text = " ".join(decrypted_text[i:i + 5] for i in range(0, len(decrypted_text), 5))
                print("Decrypted Text: {}".format(decrypted_text).lower())
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid input")
main()
