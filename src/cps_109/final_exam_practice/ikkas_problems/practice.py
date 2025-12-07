def summaryRanges(nums):
    list1 = [] 

    if not nums: 
        return list1
                
    start = nums[0]

    for i in range(1, len(nums)): 
        if nums[i] != nums[i-1] + 1: # we start and index 1 for the value of 3. Then we compare to the first number. 
             if start == nums[i-1]: # so basically lets say the first value is 1. we compare it and + 1 to it. 
                 list1.append(str(start)) # so now, we do oh "3 != 2?" well this is True and so it is not consective. so we append that single number to the list
             else: 
                 list1.append(str(start) +"->"+str(nums[i-1])) 
             start = nums[i]

    if start == nums[-1]: 
             list1.append(str(start))  
    else: 
         list1.append(str(start) +"->"+str(nums[i-1]))     

    return list1  
                    
print(summaryRanges([1, 3, 4, 6]))

