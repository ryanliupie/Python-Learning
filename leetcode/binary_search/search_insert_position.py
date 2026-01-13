def searchInsert(nums, target): 
    l, r = 0, len(nums) - 1 

    while (l <= r): 
        mid = (l + r) // 2 
        if nums[mid] < target: 
            l = mid + 1 

        elif nums[mid] > target: 
            r = mid - 1 

        else: 
            if nums[mid] == target: 
                return mid 
    
    return l

             
print(searchInsert([-1,0,2,3,4,6,8], 9))

# Example flow: 

'''
nums = [1, 3, 5, 6]
target = 4 

l = 0 
r = 2 
mid = 1, nums[mid] = 3 

is nums[mid] < target? yes so l = 2 

[1, 3, 4, 5, 6]
        ↑

we return l = 2, which gives us the value of 4. Since the target does not exist, we simply "return l"
'''