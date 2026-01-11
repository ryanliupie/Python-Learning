def twoSum(numbers, target):
    l = 0 
    r = len(numbers) - 1

    while (l < r): 
        current_sum = numbers[l] + numbers[r]

        if current_sum > target: 
            r -= 1 

        elif current_sum < target: 
            l += 1 
        
        else: 
            if current_sum == target: 
                return [l + 1, r + 1]
            

     



print(twoSum([1,2,3,4], 3)) 