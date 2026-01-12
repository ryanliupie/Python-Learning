def isValid(s):
    hashmap = {
        
               ")":"(", 
            
               "}":"{",

               "]":"["

              }
    
    stack = []

    for c in s: # iterate through the string 
        if c not in hashmap: # this line ONLY checks the KEYS!!. So since they are in the hashmap, those closing brackets (keys) are skipped.
            stack.append(c) # we only append the open brackets that are in the string. 
        
        else: 
            if not stack: # same as "if stack == []"
                return False # if there are not current opening brackets in the stack, we simply return false
            
            else:
                popped = stack.pop() 
                if popped != hashmap[c]: # compared popped char to the "value" in the hashmap, not the key 
                    return False 
    
    if stack == []: # we can also write "return not stack". we want the stack to be empty since we popped all matching characters off
        return True
    else: 
        return False 
                    



        

print(isValid("([{}])"))