def twoSum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in dict1: 
            return [dict1[target-num], i]
        dict1[num] = i 



print(twoSum([3,5,4,6], 7))