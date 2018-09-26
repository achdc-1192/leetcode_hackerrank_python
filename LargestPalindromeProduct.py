'''
Created on Sep 25, 2018
https://leetcode.com/problems/largest-palindrome-product/description/
@author: anurag varma
'''

def largestPalindrome(n):
    arr = numbergenerator(n)
    answer = 0
    product = 0
    for i in range(len(arr)):
        #print(i)
        for j in range(i+1):
            #print("array of j and i values are ", arr[j],arr[i])
            product = arr[j]*arr[i]
            print("product is ", product)
            if palindrome(product):
                if product > answer:
                    print("I am in the if condition")
                    print("product is %d and answer is %d " %(product,answer))
                    answer = product
                    print("answer is ",answer)
    print("the next coming number is the answer")
    return answer%1337

a= []
def numbergenerator(n):
    if n == 1:
        a = list(range(0,10))
    else:
        a = list(range(int('1'+'0'*(n-1)),int(str(9)*n)+1 ))
    return a

def palindrome(n):
    rev = 0
    temp = n
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n//10
    if rev == temp:
        return True


print(largestPalindrome(2))