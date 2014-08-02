from enc_dec_poly_key import *
import os, sys
import win32clipboard as wc
import win32con

def copyClipboard(string):
   if sys.platform == 'win32':
      wc.OpenClipboard()
      wc.EmptyClipboard()
      wc.SetClipboardData(win32con.CF_TEXT, string)
      wc.CloseClipboard()

print """The key must be of the form ax^2 + bx + c
where at least 'a' or 'b' != 0,
a,b,c must be integers between [0,9]"""

while True:
    option = raw_input("\nEnter 'e' for encrpytion, 'd' for decryption, or 'q' to quit: ")
    if option == 'e':
        string = raw_input("Enter text for encryption: ")
        output = enc(string)
        copyClipboard(output)
        print output
        print "Copied to your clipboard."
    elif option == 'd':
        string = raw_input("Enter text for decryption: ")
        output = dec(string)
        copyClipboard(output)
        print output
        print "Copied to your clipboard."
    elif option == 'q':
        break
