def summaryRanges(nums):
    list1 = []
    start = nums[0]
    for i in range(len(nums) - 2): 
        result = nums[i+1] - nums[i]
        if result != 1: 
            start == nums[i]
            list1.append(str(start))
    return list1
                
                




print(summaryRanges([0, 2]))

# we will do subtraction if that subtraction is equal to one, we move onto the next number 