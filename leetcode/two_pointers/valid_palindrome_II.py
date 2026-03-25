def validPalindrome(s): 
    
    def check(l, r): # regular check for palindrome  
        while (l < r): 
            if s[l] != s[r]: 
                return False 
            l += 1 
            r -= 1 
        return True
    
    l, r = 0, len(s) - 1 

    while (l < r):
         if s[l] != s[r]: 
             return check(l + 1, r) or check(l, r - 1) # we call our function and we delete the left character, then check | then delete right character, then check (this returns True or False)
         l += 1 
         r -= 1 
    
    return True

print(validPalindrome("abbda"))