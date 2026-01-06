def majorityElement(nums):
    dict1 = {}
    for num in nums: 
        dict1[num] = dict1.get(num, 0) + 1 
    
    return max(dict1, key=dict1.get)
    
print(majorityElement([5,2,1,1,1,2,5]))