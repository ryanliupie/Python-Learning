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


        

    

print(is_cyclops(675409821))
