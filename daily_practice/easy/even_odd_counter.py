def count_even_odd(numbers):
    '''
    This functions counts how many even and odd numbers are in a list.
    '''
    count_even = 0
    count_odd = 0

    for num in numbers: 
        if num % 2 == 0: 
            count_even += 1 
        else: 
            count_odd += 1
    
    return count_even, count_odd

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even, odd = count_even_odd(number_list)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")