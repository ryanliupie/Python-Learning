def safe_int_divide(a, b):
    if type(a) != int or type(b) != int: 
        raise TypeError
    elif b == 0: 
        raise ValueError
    else: 
        return a // b


print(safe_int_divide("5", 0))