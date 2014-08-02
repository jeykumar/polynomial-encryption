from enc_dec_poly_key import *
import os, sys
#import win32clipboard as wc
#import win32con
import easygui as eg


"""    
    msg = "Enter text for encryption:"
    title = "Text Encryption via Polynomial"
    string = eg.enterbox(msg, title)
    
    output = enc(string)
    #copyClipboard(output)

    msg = "Encrypted text"
    title = "Text Encryption via Polynomial"
    eg.codebox(msg, title, output)"""

msg         = "Enter encryption details"
title       = "Text Encryption via Polynomial"
fieldNames  = ["Text","a","b","c"]
fieldValues = []  # we start with blanks for the values
fieldValues = eg.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:  # do forever, until we find acceptable values and break out
    if fieldValues == None: 
        break
    errmsg = ""
    
    # look for errors in the returned values
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        
    if errmsg == "": 
        break # no problems found
    else:
        # show the box again, with the errmsg as the message    
        fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
