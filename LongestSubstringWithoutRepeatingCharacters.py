'''
Created on Aug 6, 2018
https://leetcode.com/problems/longest-substring-without-repeating-characters/
@author: anurag varma
'''


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    substr = ''; max1 = 0
    d1 = {}
    for i in range(len(s)):
        if s[i] not in substr:
            substr = substr + s[i]
        else:
            substr = s[d1[s[i]] + 1 : i + 1]
        max1 = max(max1, len(substr))
        d1[s[i]] = i
    return max1


print(lengthOfLongestSubstring("abcabcb"))

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        d={}
        output = []
        i = 0
        l = len(s)
        print("length of array is ", l)
        if l==1:
            return 1
        elif l==0:
            return 0        
        else:
            while i < l:
                #print("i value is ", i)
                if s[i] in d.keys():
                    #print("existing values of the found key is ", d[s[i]])                    
                    output.append(temp)
                    #print("output is ",output)
                    temp=[]
                    i=d[s[i]]+1
                    temp.append(s[i])               
                    #print("existing values of the i is ", i)
                    d={}                    
                    d[s[i]]=i
                    #print("d and s of i are ",d,s[i])                    
                else:
                    temp.append(s[i])
                    d[s[i]] = i
                i+=1
            output.append(temp)
        #print(d)
        #print(output)
        cur = 0
        out = 0
        for i in output:
            cur = len(i)
            if cur > out:
                out = cur
        return out
'''