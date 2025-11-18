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

def is_cyclops(n):
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
        
#---------------------------------------------------------------
        
def domino_cycle(tiles): 
    counter = 0 
    if tiles  == []: 
        return True 
    
    for i in range(len(tiles) - 1): 
        if tiles[i][1] == tiles[i+1][0]: 
             counter += 1
        
    
    if tiles[-1][-1] == tiles[0][0]: 
            counter += 1
    

    if counter == len(tiles): 
         return True
    return False

            
print(domino_cycle([(3, 5), (5, 2), (2, 4)]))   


#---------------------------------------------------------------

"""def count_dominators(items):
    counter = 0
    
    for i in range(len(items)):
        j = i + 1 
        
        while j < len(items): 
            if items[j] >= items[i]:
                break 
            j += 1 
            
        if j == len(items): 
            counter += 1 
            
    return counter
"""
#---------------------------------------------------------------

def extract_increasing(digits):
    list1 = []
    previous = -1 
    current = 0 
    
    for char in digits: 
        int_char = int(char)
        current = 10 * current + int_char # 10 * 0 + 3 = 3 
    
        if current > previous: 
            list1.append(current)
            previous = current 
            current = 0 
    
    return list1
        
    
print(extract_increasing("345349"))

