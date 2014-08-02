from math import sqrt

def getKey():
    a = int(raw_input("a = "))
    b = int(raw_input("b = "))
    c = int(raw_input("c = "))
    key = {'a': a, 'b': b, 'c': c}
    return key

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
    key = getKey()
    a = key['a']
    b = key['b']
    c = key['c']
    newString = ''
    for i in string:
        x = ord(i)
        x = a*(x**2)+ b*(x) + c
        newString += (str(x) + '#')
    return shuffle(newString)

def read(string):
    newString = string[:-1]
    return newString.split('#')        

def dec(string):
    key = getKey()
    a = key['a']
    b = key['b']
    c = key['c']
    string = shuffle(string)
    newString = ''
    charList = read(string)
    for i in range(len(charList)):
        charList[i] = int(charList[i])
    for i in charList:
        x = int((-b+sqrt((b**2)-4*(a)*(c-i)))/(2*a))
        newString += chr(x)
    return newString

def copyClipboard(string):
   if sys.platform == 'win32':
      wc.OpenClipboard()
      wc.EmptyClipboard()
      wc.SetClipboardData(win32con.CF_TEXT, string)
      wc.CloseClipboard()
