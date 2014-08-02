from enc_dec_poly import *

while True:
    option = raw_input("Enter 'e' for encrpytion, 'd' for decryption, or 'q' to quit: ")
    if option == 'e':
        string = raw_input("Enter text for encryption: ")
        print enc(string)
    elif option == 'd':
        string = raw_input("Enter text for decryption: ")
        print dec(string)
    elif option == 'q':
        break
