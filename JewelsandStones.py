'''
Created on Jul 29, 2018

@author: anurag varma
https://leetcode.com/problems/jewels-and-stones/description/

'''
def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    l = []
    count = 0
    for i in range(len(J)):
        l.append(J[i])
    for j in range(len((S))):
        if S[j] in l:
            count += 1
    return count

print(numJewelsInStones("aA", "aAAZZss"))

'''
Alternate one liner found in comments
def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105
def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
'''