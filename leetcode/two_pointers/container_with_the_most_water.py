def maxArea(heights):
    l = 0 
    r = len(heights) - 1

    res = 0 

    while (l < r): 
        area = min(heights[l], heights[r]) * (r - l) # shorter wall limits the area otherwise there is an overflow. 
        res = max(res, area) # we are keeping the count. we don't add anything to res, it just replaces the highest area each iteration. 

        if heights[l] <= heights[r]: # we move through each value. on iteration 3, area is 15. res = (36, 15). res still the same (36). we keep going and return max res at the end. 
            l += 1 
        else: 
            r -= 1 
    
    return res
    
print(maxArea([1,7,2,5,4,7,3,6]))
    
