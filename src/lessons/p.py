def two_summers(items, target):
    left = 0 
    right = len(items) - 1

    while left < right:
        result = items[left] + items[right] 
        if result == target: 
            return tuple((items[left], items[right]))
        elif result < target: 
            left += 1 
        else: 
            right -= 1 

print(two_summers([1, 2, 3, 4, 5], 7))
        