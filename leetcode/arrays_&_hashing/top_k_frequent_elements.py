def topKFrequent(nums):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1 

    return hashmap 



print(topKFrequent([1,2,2,3,3,3]))
 
