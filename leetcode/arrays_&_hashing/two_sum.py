def twoSum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in dict1: 
            return [dict1[target-num], i]
        dict1[num] = i 

# we find the complement 
# 7 - 3 = 4. is 4 in dict1? no, we add so dict1[num] = i so {3:0}, note i is the index
# 7 - 5 = 2. is 2 in dict1? no, we add so {5:0}
# 7 - 4 = 3.  is 3 in dict11? YES!

# we then return[dict1[target-num], i]
# [dict[7-4], 2]
# [dict1[3], 2] 

# so dict1[3] corresponds to "0"
# and 2 corresponds to the actual index so we return 2

print(twoSum([3,5,4,6], 7))