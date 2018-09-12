'''
Created on Aug 5, 2018
https://leetcode.com/problems/longest-palindrome/description/
@author: anurag varma
'''
def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    count = 0
    for letter in s:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1
    for key in d:
        if d[key] % 2 == 0:
            count += d[key]
        else:
            count += d[key] - 1
        
    if count==len(s):
        return count
    else:
        return count + 1

s = "abcd"

print(longestPalindrome(s))