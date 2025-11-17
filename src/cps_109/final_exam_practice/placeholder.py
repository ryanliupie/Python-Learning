def extract_increasing(digits):
    list1 = []
    previous = -1 
    current = 0 
    
    for char in digits: 
        int_char = int(char)
        current = 10 * current + int_char
        
        if current > previous:
            list1.append(current)
            previous = current 
            current = 0 
    return list1

print(extract_increasing("7777777777777777777"))
                    

