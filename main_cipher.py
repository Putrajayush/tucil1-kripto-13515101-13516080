def main():
    print("tes")
    type = int(input("1. Vigenere cipher\n2. Full Vigenere cipher\n3. Auto-key Vigenere cipher\n4. Extended Vigenere cipher\n5. Super cipher\n6. Playfair cipher\n7. Affine cipher\n8. Hill cipher\nChoose:"))
    if type == 1:
        import vigenere_cipher
    elif type == 2:
        import full_vigenere_cipher
    elif type == 3:
        import auto_key_cipher
    elif type == 4:
        import extended_vigenere_cipher
    elif type == 5:
        import super_cipher
    elif type == 6:
        import playfair_cipher
    elif type == 7:
        import affine_cipher
    elif type == 8:
        import hill_cipher
    else:
        print("Input Invalid")

main()
