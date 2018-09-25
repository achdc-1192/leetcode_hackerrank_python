'''
Created on Sep 24, 2018
https://leetcode.com/problems/rotate-array/description/
@author: anurag varma
'''
def rotate(nums, k):
    if k > len(nums):
        k=k%len(nums)
    for _ in range(len(nums)-k):
        nums.append(nums[0])
        nums.pop(0)
    #print(nums)
    return nums


    '''
    print("value of rotation mod is ",rotation_mod)
    print("length of nums is ", len(nums))
    output = [0 for i in range(len(nums))]
    for i in range(len(nums)):
            output[(rotation_mod+i)%len(nums)]=nums[i]
    return output
    '''
    return nums

print(rotate([-1,-100,3,99,1,2], 2))
print(rotate([1,2,3,4,5,6,7],3))