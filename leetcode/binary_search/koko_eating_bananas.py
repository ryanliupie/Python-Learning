from math import ceil # ceil rounds a number up to the nearest integer
'''
def minEatingSpeed(piles, h): 

    # I believe my solution works, but it is way too slow. 

    rate = 1 

    while True: 
        count = 0

        for i in range(len(piles)): 
            res = piles[i]

            while res > 0: 
                res = res - rate 
                count += 1 

        if count <= h: 
            return rate
        
        rate += 1 

print(minEatingSpeed([1, 4, 3, 2], 9))
'''

def minEatingSpeed(piles, h): 
    def k_works(k): 
        hours = 0 

        for p in piles: 
            hours += ceil(p/k)
        
        return hours <= h
    
    l = 1 # same as rate = 1 
    r = max(piles) # highest possible rate 

    while (l < r): 
        k = (l + r) // 2

        if k_works(k):
            r = k 
        else: 
            l = k + 1 
    
    return r 

print(minEatingSpeed([1, 4, 3, 2], 9))
    