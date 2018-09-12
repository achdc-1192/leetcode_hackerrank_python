'''
Created on Jul 30, 2018
https://leetcode.com/problems/flipping-an-image/description/
@author: anurag varma
'''
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    output=[]
    for l in A:
        l=l[::-1]
        for item in range(len(l)):
            print("item is ",item)
            print("l[item] before xoring is",l[item])
            l[item]=l[item]^1
        print("l ",l)
        output.append(l)
    return output

A= [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(A))
