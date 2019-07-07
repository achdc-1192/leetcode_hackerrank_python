def removeDuplicates(nums):
    i = 0
    j = 0
    if len(nums)== 0:
        return 0
    while j < len(nums):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i += 1
        j += 1
    print(nums)
    return i+1

nums=[1,1,2,2,3,4,5,5,5,6,7,8]
print(removeDuplicates(nums))