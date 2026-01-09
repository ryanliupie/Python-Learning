def isPalindrome(s): 
    l = 0 
    r = len(s) - 1 

    while (l < r):  
        while (l < r) and not s[l].isalnum(): 
            l += 1 
        while (l < r) and not s[r].isalnum(): 
            r -= 1
    
        if s[l].lower() != s[r].lower(): # only runs when we reach a value that is (a-z) or (0-9). Then it checks whether they are equal to each other or not 
            return False 

        l += 1 # now if the "if" doesn't return false, that means we are good and so we will continue to move in. 
        r -= 1 # once the condition reaches "while (l<r)", we return true since its a valid palindrome. 
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))