#Swap every two consecutive characters
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
        
