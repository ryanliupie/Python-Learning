new_list = [1, 3, 3, 4, 6]

for i in range(len(new_list) - 1): 
    result = new_list[i+1] - new_list[i]
    if result == 1: 
        print(True)
    else: 
        print(False)


