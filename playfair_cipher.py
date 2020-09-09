import string

def remove(string): 
    return string.replace(" ", "")

#Making Key Matrix
def key_matrix_generation(key):
    atoz = string.ascii_lowercase.replace('j', '.')
    
    key_matrix = ['' for i in range(5)]

    i = 0
    j = 0

    for c in key:
        if c in atoz:
            key_matrix[i] += c
            atoz = atoz.replace(c, '.')            
            j += 1
            if j > 4:
                i += 1
                j = 0

    for c in atoz:
        if c != '.':
            key_matrix[i] += c
            j += 1
            if j > 4:
                i += 1
                j = 0
    return key_matrix


#Encryption function
def playfair_encrypt(plaintext, plaintextpairs, key_matrix):    
    i = 0
    ciphertext = ""
    ciphertextpairs = []

    while i < len(plaintext):
        a = plaintext[i]
        b = ''
        if i + 1 == len(plaintext):
            b = 'x'
        else:    
            b = plaintext[i+1]

        if a!= b:
            plaintextpairs.append(a + b)
            i += 2
        else:
            plaintextpairs.append(a + 'x')
            i += 1

    print(plaintextpairs)


    #RULE 2
    #Jika pasangan huruf muncul di row yang sama
    #Tukar dengan yang ada di sebelah kanan tiap huruf

    for pair in plaintextpairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                ciphertextpair = row[(j0 + 1)%5] + row[(j1 + 1)%5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True

        if applied_rule:
            continue
        
        #RULE 3
        #Jika pasangan huruf muncul di column yang sama
        #Tukar dengan yang ada di bawah tiap huruf
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                ciphertextpair = col[(i0 + 1)%5] + col[(i1 + 1)%5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True

        if applied_rule:
            continue

        #RULE 4
        #Tukar pasangan huruf dengan huruf yang ada di sudut
        #Dari segiempat yang dibentuk kedua huruf pada matrix
        # Huruf pertama = baris huruf pertama, kolom huruf kedua
        # Huruf kedua = baris huruf kedua, kolom huruf pertama
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
                
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        ciphertextpairs.append(ciphertextpair)

    return ciphertextpairs

#Decryption function
def playfair_decrypt(ciphertext, ciphertextpairs, key_matrix):    
    i = 0
    plaintext = ""
    plaintextpairs = []

    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1]
        
        ciphertextpairs.append(a + b)
        i += 2

    print(ciphertextpairs)


    #RULE 2
    #Jika pasangan huruf muncul di row yang sama
    #Tukar dengan yang ada di sebelah kanan tiap huruf

    for pair in ciphertextpairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                plaintextpair = row[(j0 + 4)%5] + row[(j1 + 4)%5]
                plaintextpairs.append(plaintextpair)
                applied_rule = True

        if applied_rule:
            continue
        
        #RULE 3
        #Jika pasangan huruf muncul di column yang sama
        #Tukar dengan yang ada di bawah tiap huruf
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                plaintextpair = col[(i0 + 4)%5] + col[(i1 + 4)%5]
                plaintextpairs.append(plaintextpair)
                applied_rule = True

        if applied_rule:
            continue

        #RULE 4
        #Tukar pasangan huruf dengan huruf yang ada di sudut
        #Dari segiempat yang dibentuk kedua huruf pada matrix
        # Huruf pertama = baris huruf pertama, kolom huruf kedua
        # Huruf kedua = baris huruf kedua, kolom huruf pertama
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
                
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        plaintextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        plaintextpairs.append(plaintextpair)
        
    return plaintextpairs


def main():
    mode = int(input("1. Type Text\n2. Input File\nChoose(1,2): "))
    if mode == 1:
        msg = input("Enter Message: ").lower()
        msg = remove(msg)
        keycode = input("Enter Key: ").lower()
        matrix = key_matrix_generation(str(keycode))

        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:
            
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                pairs = []
                encrypt_result = playfair_encrypt(msg, pairs, matrix)
                print("ciphertext: " + "".join(encrypt_result))
            elif space == 2:
                print("--Encryption--")
                pairs = []
                encrypt_result = playfair_encrypt(msg, pairs, matrix)
                str1 = ""
                encrypt_result = str1.join(encrypt_result)
                encrypt_result= " ".join(encrypt_result[i:i + 5] for i in range(0, len(encrypt_result), 5))
                print("ciphertext: " + "".join(encrypt_result))
            else:
                print("Invalid Input")

        elif choice == 2:

            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                pairs = []
                decrypt_result = playfair_decrypt(msg, pairs, matrix)
                print("plaintext: " + "".join(decrypt_result))
            elif space == 2:
                print("--Decryption--")
                pairs = []
                decrypt_result = playfair_decrypt(msg, pairs, matrix)
                str1 = ""
                decrypt_result = str1.join(decrypt_result)
                decrypt_result= " ".join(decrypt_result[i:i + 5] for i in range(0, len(decrypt_result), 5))
                print("plaintext: " + "".join(decrypt_result))
            else:
                print("Invalid Input")

        else:
            print("Invalid input")

            
    elif mode == 2:
        infile_name = input("Enter input file name: ")
        infile = open(infile_name, 'r+')

        msg = infile.read()
        msg = remove(msg).lower()
        keycode = input("Enter Key: ").lower()

        matrix = key_matrix_generation(str(keycode))

        choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
        if choice == 1:
            
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Encryption--")
                pairs = []
                encrypt_result = playfair_encrypt(msg, pairs, matrix)
                print("ciphertext: " + "".join(encrypt_result))

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(encrypt_result)
                else:
                    pass
                
            elif space == 2:
                print("--Encryption--")
                pairs = []
                encrypt_result = playfair_encrypt(msg, pairs, matrix)
                str1 = ""
                encrypt_result = str1.join(encrypt_result)
                encrypt_result= " ".join(encrypt_result[i:i + 5] for i in range(0, len(encrypt_result), 5))
                print("ciphertext: " + "".join(encrypt_result))

                save = int(input("1. Save message to file\n2. Dont Save\nChoose(1,2):"))
                if save == 1:
                    infile.write(encrypt_result)
                else:
                    pass
            else:
                print("Invalid Input")

        elif choice == 2:
            
            space = int(input("1. No space\n2. Space every 5 char\nChoose(1,2):"))
            if space == 1:
                print("--Decryption--")
                pairs = []
                decrypt_result = playfair_decrypt(msg, pairs, matrix)
                print("plaintext: " + "".join(decrypt_result))
            elif space == 2:
                print("--Decryption--")
                pairs = []
                decrypt_result = playfair_decrypt(msg, pairs, matrix)
                str1 = ""
                decrypt_result = str1.join(decrypt_result)
                decrypt_result= " ".join(decrypt_result[i:i + 5] for i in range(0, len(decrypt_result), 5))
                print("plaintext: " + "".join(decrypt_result))
            else:
                print("Invalid Input")

        else:
            print("Invalid input")

            
    else:
        print("Invalid Input")

main()
