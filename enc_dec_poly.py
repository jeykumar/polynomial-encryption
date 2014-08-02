from math import sqrt

def lenEven(string):
    if len(string) % 2 == 0:
        return True
    else:
        return False

def shuffle(string):
    length = len(string)
    if lenEven(string):
        s = list(string)
        sCopy = list(s)
        for i in range((length+1)/2):
            s[2*i] = sCopy[2*i+1]
            s[2*i+1] = sCopy[2*i]
        return "".join(s)
    if not lenEven(string):
        s = list(string[:-1])
        sCopy = list(s)
        for i in range((length)/2):
            s[2*i] = sCopy[2*i+1]
            s[2*i+1] = sCopy[2*i]
        return "".join(s) + string[-1]

def enc(string):
    newString = ''
    for i in string:
        x = ord(i)
        x = x**2 + 3
        newString += (str(x) + '#')
    return shuffle(newString)

def read(string):
    newString = string[:-1]
    return newString.split('#')        

def dec(string):
    string = shuffle(string)
    newString = ''
    charList = read(string)
    for i in range(len(charList)):
        charList[i] = int(charList[i])
    for i in charList:
        x = int(sqrt(i-3))
        newString += chr(x)
    return newString
