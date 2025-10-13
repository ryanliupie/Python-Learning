# --------------------------------------------------------------
# 1) Mixed Fractions
# --------------------------------------------------------------

def mixedfraction(num, den):

    '''
    This function accepts an integer fraction, in the form of a
    numerator and a denominator. You may assume both numerator
    and denominator are non-negative.
    
    It returns a mixed fraction, 
    represented using a 3-tuple. The whole number is the first
    element, and the numerator and denominator of the remaining
    fraction are the 2nd and 3rd elements, respectively.
    
    For example:
    mixedfraction(7, 3) should return (2, 1, 3) 
    mixedfraction(4, 5) should return (0, 4, 5) 
    mixedfraction(9, 3) should return (3, 0, 3) 
    
    If the denominator is 0, return None.
    '''
    if den == 0: 
        return None
    
    else: 
        fraction = tuple()
        result1 = num // den 
        result2 = num % den 
        denominator = den 

        fraction = result1, result2, denominator

        return fraction


# --------------------------------------------------------------
# 2) Cyclops Numbers
# --------------------------------------------------------------

def iscyclops(n):

    '''
    A non-negative integer is said to be a cyclops number if it 
    consists of an odd number of digits, the middle digit 
    (more poetically, the “eye”) is a zero, and all other 
    digits of that number are non-zero.

    Return True if the input is a cyclops number, and False
    otherwise.

    Note 1: Functions that return True/False are unlikely to 
    appear on a test, since you can achieve at least 50% by
    simply saying 'return True' or 'return False'...

    Note 2: This problem comes from Ilkka Kokkarinen's 
    excellent set of "109 Python Problems for CCPS 109". The 
    full set can be found at his github, and are great practice.

    https://github.com/ikokkari/PythonProblems

    Many (or most) of his problems are quite difficult, so be
    ready for a challenge if you attempt them.

    '''

    counter = 0 
    nums = str(n)

    if len(nums) % 2 == 0: 
        return False 
    
    for char in nums: 
        if char == "0": 
            counter += 1 
        
        if counter > 1: 
            return False

    else: 
        x = len(nums) // 2 
        if nums[x] == "0": 
            return True
        
        return False


# --------------------------------------------------------------
# 3) Parity Partition
# --------------------------------------------------------------

def paritypartition(items):

    '''
    This function accepts a list of integers, and returns a list
    containing the exact same integers, but separated by even
    and odd. All the even numbers should be at the front of the 
    list, and all the odd numbers should be at the back.

    The relative order of the even numbers should be the same
    as the original list. The same applies to the odd numbers.

    For example, given the input list:  [7, 0, 4, -1, 3, 2, 1]
    this function should return:        [0, 4, 2, 7, -1, 3, 1] 

    '''

    even_list = []
    odd_list = []
    main_list = []

    for num in items: 
        if num % 2 == 0: 
            even_list.append(num)
        
        else:  
            odd_list.append(num)
    
    main_list = even_list + odd_list
    return main_list


# --------------------------------------------------------------
# 4) Alternating Sign Sum
# --------------------------------------------------------------

def altsignsum(items):

    '''
    This function accepts a list of positive numeric values, and 
    returns the alternating sign sum. 
    This means that elements in even index positions are added, 
    and elements at odd indexes are subtracted. For example:

    altsignsum([3, 5, 2, 4, 8, 2]) should return 2
    3 - 5 + 2 - 4 + 8 - 2 = 2

    If the input is the empty list, return 0

    ''' 

    counter = 0 
    i = 0 
    if items == []: 
        return 0 
    
    else: 
        while i < len(items): 
            if i % 2 == 0:
                counter += items[i]
                i += 1 

            else: 
                if i % 2 != 0: 
                    counter -= items[i]
                    i += 1 
        
        return counter


# --------------------------------------------------------------
# 5) Domino Cycle
# --------------------------------------------------------------

def domninocycle(tiles):

    '''
    This is another from Ilkka's problem set.

    A single domino tile is represented as a two-tuple of its 
    pip values, such as (2,5) or (6,6). This function should 
    determine whether the given list of tiles forms a cycle so 
    that each tile in the list ends with the exact same pip value 
    that its successor tile starts with, the successor of the 
    last tile being the first tile of the list since this is 
    supposed to be a cycle instead of a chain. 
    
    Return True if the given list of tiles forms such a cycle, 
    and False otherwise.

    For example, for the input  [(3, 5), (5, 2), (2, 3)], this
    function should return True.

    For the input [(2, 5), (5, 2), (2, 3)], this function 
    returns False because the first value on the first tile (2)
    does not match the 2nd value on the last tile (3)
    
    '''

    if tiles == []: 
        return True

    for i in range(len(tiles) - 1): 
        if tiles[i][1] != tiles[i + 1][0]: 
            return False
         
    if tiles[-1][1] != tiles[0][0]: 
        return False
    
    return True

