def simplify_path(path): 
    list1 = path.split("/")
    stack = []
    for str in list1: 
        if str == "..":
            if stack: # once we come across an element, this checks "are there elements in the list". if so, we pop the most recent 
                stack.pop() # item that was recently added gets popped off. This follows the ".." logic where we go up a directory
        
        elif str != "" and str != ".": 
            stack.append(str)

    return "/" + "/".join(stack)


print(simplify_path("/home/user/Documents/../Pictures"))