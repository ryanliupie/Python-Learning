def findMin(nums): 
    l, r = 0, len(nums) - 1 

    while (l < r): 
        mid = (l + r) // 2

        if nums[mid] > nums[r]: 
            l = mid + 1 
        else: 
            r = mid 
    
    return nums[l]

print(findMin([4, 5, 6, 7, 0, 1, 2]))

'''
for example the array nums = [0, 1, 2, 4, 5, 6, 7]

- rotated 4 times array nums = [4, 5, 6, 7, 0, 1, 2]

- rotated 7 times array nums = [0, 1, 2, 4, 5, 6, 7]

so is most instances, there is a pivot point straight from increasing to decreasing. 

nums = [4, 5, 6, 7, 0, 1, 2]
        0  1  2  3  4  5  6   

if nums[mid] > nums[r]:
    l = mid + 1
else:
    r = mid

When nums[mid] > nums[r]: 

- the minimum must be on the right side
- because mid is in the bigger, left sorted portion
- so we must do l = mid + 1 

But lets say when nums[mid] <= nums[r]

- this means the section from mid to r is sorted (0, 1, 2 in the example above)
- so the minimum is not to the right of mid 
- but it could be mid itself 

Once l = r, the search space collapses to one single element, therefore there is nothing left to compare
''' 