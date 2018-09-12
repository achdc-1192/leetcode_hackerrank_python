'''
Created on Jul 29, 2018

@author: anurag varma
'''


def toLowerCase(st):
    """
    :type str: str
    :rtype: str
    """
    s = ""
    for i in st:
        if ord(i) >= 65 and ord(i) <= 90:
            s += chr(ord(i) + 26 + 6)
        else:
            s += i
    return s

print(toLowerCase("LOVELY"))