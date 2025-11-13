# -*- coding: utf-8 -*-

def ryerson_letter_grade(n): 
    if 0 <= n <= 49: 
        return "F"
    elif 50 <= n <= 52: 
        return "D-"
    elif 53 <= n <= 56: 
        return "D"
    elif 57 <= n <= 59: 
        return "D+"
    elif 60 <= n <= 62: 
        return "C-"
    elif 63 <= n <= 66: 
        return "C"
    elif 67 <= n <= 69: 
        return "C+"
    elif 70 <= n <= 72: 
        return "B-"
    elif 73 <= n <= 76: 
        return "B"
    elif 77 <= n <= 79: 
        return "B+"
    elif 80 <= n <= 84: 
        return "A-"
    elif 85 <= n <= 89: 
        return "A"
    elif n>= 90: 
        return "A+"
    
#---------------------------------------------------------------
    
def is_ascending(items):
    counter = 0 
    for i in range(len(items) - 1): 
        if items[i+1] > items[i]: 
            counter += 1 
            
    if counter == len(items) - 1: 
        return True
    return False
    
#---------------------------------------------------------------

def riffle(items, out=True): # function may be set to "out=False" so we simply flip the first and second half
    main_list = []
    
    mid = len(items) // 2 
    first_half = items[:mid]
    second_half = items[mid:]
    
    
    if out == True: 
        
        for i in range(len(first_half)): 
            main_list.append(first_half[i])
            main_list.append(second_half[i])
    
        return main_list
    
    else: 
        
        for i in range(len(second_half)): 
                main_list.append(second_half[i])
                main_list.append(first_half[i])
        
        return main_list
    
#---------------------------------------------------------------

def only_odd_digits(n): # convert to string, then if value not in n, take off, and then compare the lengh of the string to the original
     counter = 0 
     first_list = []
     str_n = str(n)
     for char in str_n: 
         first_list.append(char)
     
     for num in first_list: 
        if int(num) % 2 != 0: 
            counter += 1 
 
     if counter == len(first_list): 
        return True 
     return False

print(only_odd_digits(0))    
    
# counter = 5 
# len of list = 5

# if they match, return True 


#---------------------------------------------------------------

new_list = []
    counter = 0 
    positive_nums = abs(n)
    str_n = str(positive_nums)
    if len(str_n) % 2 == 0: 
        return False
    else: 
        for char in str_n: 
            new_list.append(char)
        for num in str_n: 
            if num == "0": 
                counter+= 1 

        if counter > 1: 
            return False
        else: 
            mid = len(str_n) // 2
            if str_n[mid] == "0": 
                return True
            return False