def longestConsecutive(nums): 
    set1 = set(nums)
    max_len = 0

    for num in set1: 
        if num - 1 not in set1:
            curr_num = num
            curr_len = 1 
            while curr_num + 1 in set1:
                curr_len += 1 
                curr_num += 1 
            max_len = max(max_len, curr_len)

    return max_len

print(longestConsecutive([0,3,2,5,4,6,1,1]))