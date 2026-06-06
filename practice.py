def largest(nums): 
    biggest = nums[0]

    for num in nums: 
        if num > biggest: 
            biggest = num 
    
    return biggest

print(largest([5,2,9,1]))


def another(nums): 
    sorted_nums = sorted(nums)
    return sorted_nums[-1]

print(another([5,2,9,1]))



def another1(nums): 
    array = dict()
    for num in nums:
        array[num] = array.get(num, 0) + 1

    result = []
    for key in array.keys(): 
        result.append(key)
    
    sorted_nums = sorted(result)
    return sorted_nums[-1]
    
print(another1([5,2,9,1]))