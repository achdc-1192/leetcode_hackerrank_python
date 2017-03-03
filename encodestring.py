# your code goes
import re
from collections import OrderedDict
def encodestring(s):
    s = re.sub("[aeiou]+","",s)
    if s == "":
        return ""
    s = "".join(OrderedDict.fromkeys(s))
    l = list(s)
    if len(l)==1:
        return s
    elif len(l) == 2:
        x = ord(l[0])%97
        y = ord(l[1])%97
        z = x+y
        z = chr(z%26+97+1)
        l[0] = z
        l[1] = z
        return "".join(l)
    else:
        for i in range(len(l)):
            if i==len(l)-1:
                x = ord(l[i])%97 + ord(s[0])%97
                l[i] = chr(x%26+97+1)
                #print l[i]
            else:
                x = ord(l[i])%97 + ord(l[i+1])%97
                l[i] = chr(x%26+97+1)
                #print l[i]
        return "".join(l)
print encodestring("yxyxyxioioio")
