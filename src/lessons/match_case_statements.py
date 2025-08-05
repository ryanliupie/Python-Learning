# Match-Case statement (Switch): This is an alternative to 
#                                using many "elif" statements

def rainbow(colour):
    if colour == "Red":
        return f"Your favourite colour is {colour}"

    elif colour == "Blue":
        return f"Your favourite colour is {colour}"

    elif colour == "Green":
        return f"Your favourite colour is {colour}"

    elif colour == "Pink":
        return f"Your favourite colour is {colour}"
    
    else:
        print("Lol choose a different colour")

print(rainbow("Red"))

# -----------------------------------------------------------

def rainbow(colour):
    match colour:
        case "Red":
            return f"Your favourite colour is {colour}"
        
        case "Blue":
            return f"Your favourite colour is {colour}"
        
        case "Green":
            return f"Your favourite colour is {colour}"
        
        case "Pink":
            return f"Your favourite colour is {colour}"
        
        case _:
            return "Lol choose a different colour"
        
print(rainbow("Blue"))