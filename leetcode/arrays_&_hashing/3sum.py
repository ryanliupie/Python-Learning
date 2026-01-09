def threeSum(nums):
    list1 = []
    nums.sort()

    for i in range(len(nums)):
        if i!= 0 and nums[i] == nums[i-1]: 
            continue 

        # perform a two sum II on the remainder portion
        # we sorted the list, so this is possible 
        l = i + 1 
        r = len(nums) - 1

        while (l < r): 
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum > 0: 
                r -= 1 
            elif current_sum < 0: 
                l += 1
            else: 
                if current_sum == 0: 
                    list1.append([nums[i], nums[l], nums[r]])
                    l += 1 

                while (l < r) and nums[l] == nums[l-1]: 
                    l += 1
        
    return list1

print(threeSum([-1,0,1,2,-1,-4]))