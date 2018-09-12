'''
Created on Aug 5, 2018
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
@author: anurag varma
'''
'''
def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp = []
    output = []
    j = 0
    l = len(nums)
    print("length of array is ", l)
    if l==1:
        return 1
    elif l==0:
        return 0
    else:
        for i in range(j,l-1):
            print("i, nums[i] and nums[i+1] are ", i,nums[i],nums[i+1])
            if nums[i] < nums[i+1]:
                temp.append(nums[i])
                print("temp in if  is ",temp)
            else:
                temp.append(nums[i])
                print("temp in else is ", temp)
                output.append(temp)
                temp=[]
                j=i+1
        print(nums[i+1])
        temp.append(nums[i+1])
        output.append(temp)
    count = 0
    cur = 0
    for i in output:
        count = len(i)
        if count > cur:
            cur = count
    return cur
'''


def findLengthOfLCIS(nums):
    ans = 0
    count = 1
    for i in range(0,len(nums)-1):
        if nums[i] < nums[i+1]:
            count += 1
        else:
            count = 1
        ans = max(ans,count)
    return ans

nums=[1,2,3,1,2,3,4,5]
print(findLengthOfLCIS(nums))