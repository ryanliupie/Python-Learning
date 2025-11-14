def colour_trio(colours):
    all_colours = ["r", "y", "b"]
    list1 = []
    new_list = []
    
    for char in colours: 
        list1.append(char)
    
    for i in range(len(list1) - 1): 
        if list1[i] != list1[i+1]:
            pair = list1[i], list1[i+1]
            
            for colour in all_colours: 
                if colour not in pair: 
                    new_list.append(colour)
        else: 
            if list1[i] == list1[i+1]:
                new_list.append(list1[i])
    return new_list


    

                 
            
        
        
    
    
    

print(colour_trio("rybyry"))
