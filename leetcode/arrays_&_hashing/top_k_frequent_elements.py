def topKFrequent(nums):
    hashmap = {}

    for num in nums: 
        hashmap[num] = hashmap.get(num, 0) + 1 # {1: 1: 2: 3, 3: 3}

    reversed_dict = {}
    for key, value in hashmap.items(): 
        if value not in reversed_dict: 
            reversed_dict[value] = []
        reversed_dict[value].append(key) # {1: [1], 2: [2, 3]} | these are now frequencies (how many times they appear)
        
    reversed_sort = dict(sorted(reversed_dict.items(), reverse=True)) # {2: [2, 3], 1: [1]} | we reverse it so highest key first

    result = []
    for freq in reversed_sort: # access key 
        for num in reversed_sort[freq]: # access values for each key
            result.append(num)
            if len(result) == k: 
                return result 
print(topKFrequent([1,2,2,3,3,3]))
 
# bucket sort is probably the best way to solve this problem though