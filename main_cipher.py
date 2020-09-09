def main():
    print("tes")
    type = int(input("1. Vigenere cipher\n2. Full Vigenere cipher\n3. Auto-key Vigenere cipher\n4. Extended Vigenere cipher\n5. Super cipher\n6. Playfair cipher\n7. Affine cipher\n8. Hill cipher\nChoose:"))
    if type == 1:
        import vigenere_cipher
        vigenere_cipher.main()
    elif type == 2:
        import full_vigenere_cipher
        full_vigenere_cipher.main()
    elif type == 3:
        import auto_key_cipher
        auto_key_vigenere_cipher.main()
    elif type == 4:
        import extended_vigenere_cipher
        extended_vigenere_cipher.main()
    elif type == 5:
        import super_cipher
        super_cipher.main()
    elif type == 6:
        import playfair_cipher
        playfair_cipher.main()
    elif type == 7:
        import affine_cipher
        affine_cipher.main()
    elif type == 8:
        import hill_cipher
        hill_cipher.main()
    else:
        print("Input Invalid")

main()
