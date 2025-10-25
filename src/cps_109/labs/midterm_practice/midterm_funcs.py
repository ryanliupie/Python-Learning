# --------------------------------------------------------------
# CODING PROBLEMS: 
# --------------------------------------------------------------

'''

Fill in the functions below according to their descriptions. Test
your code by running the file "midterm_tests.py"

Make sure your code compiles before you finish the test, do NOT 
leave syntax errors in your code! This is VERY important.

You don't need to submit on D2L. Just save your code locally. Be
sure to fill in your full name and email below:

FULL NAME: <your name here>
TMU EMAIL: <your email here>

'''

# Q1) 
def roman_to_arabic(rn):
    '''
    rn is a string representing a roman numeral. Your program should convert
    this number to an arabic base-10 integer, and return it. Your function
    only has to work for first 10 roman numerals. If rn is not one of the first
    10 numerals, return None. The first 10 roman numerals are given below:

    I    = 1
    II   = 2
    III  = 3
    IV   = 4
    V    = 5
    VI   = 6
    VII  = 7
    VIII = 8
    IX   = 9
    X    = 10
    '''
    
    dict1 = {"I": 1,  
            "II": 2,  
            "III": 3,  
            "IV": 4,  
            "V": 5,  
            "VI": 6,  
            "VII": 7,  
            "VIII": 8,  
            "IX": 9,  
            "X": 10 
        }
    
    if rn in dict1.keys():
        return dict1[rn]


# Q2)
def sum_even(n):
    '''
    Assume n is an integer >= 1.
    Return the sum of the integers, between 1-n inclusive, 
    that are even
    '''

    sum_list = []
    for num in range(1, n+1): 
        if num % 2 == 0: 
            sum_list.append(num)

    return sum(sum_list)
    
    


# Q3)
def integers_exceed(n):
    '''
    How many consecutive integers, starting at 1, must be
    added before the sum exceeds n?
    For example, if n is 11, we must add 1+2+3+4+5 = 15,
    and therefore the answer is 5.
    '''

    counter = 0 
    total_sum = 0 
    num = 1 

    while total_sum <= n: 
        total_sum += num
        counter += 1
        num += 1 
    
    return counter 
 

        
# Q4)
def pyramid_blocks(n, m):
    '''
    Assume n and m are integers >= 1.
    Consider a solid rectangular pyramid, whose base is n-by-m 
    blocks. The layer above is (n-1)-by-(m-1), and so on. The top 
    layer will be n-by-1, or 1-by-m, depending on which dimension 
    reaches 1 first. Assume n and m are integers. Return the number 
    of blocks in the pyramid.
    '''
    counter = 0 
    
    while n > 0 and m > 0: 
        x = n * m 
        counter += x 
        n = n - 1 
        m = m - 1 
    
    return counter 


# Q5)
def first_letter(digits):
    '''
    Assume that digits is a string containing numeric digits.
    Returns a string whose corresponding characters are the first 
    letter of each digit.
    For example: '5113' returns 'foot',  since the first letters 
    of five, one, one, three are f, o, o, t.  
    Similarly, '0123456789613' returns 'zottffssensot'.
    '''

    new_str = ""
    dict1 = {"0": "z",
             "1": "o", 
             "2": "t", 
             "3": "t",
             "4": "f", 
             "5": "f", 
             "6": "s", 
             "7": "s",
             "8": "e", 
             "9": "n"
             }
    
    for num in digits:
        if num in dict1.keys(): 
            new_str = new_str + dict1[num]
    
    return new_str


# Q6) 
def deduplicate(s):
    '''
    Assume that s is a string.
    Return a new string that is the same as s, but with consecutive 
    duplicate characters removed. For example, 'feeder' returns 'feder' 
    since it changes the 'ee' to 'e'.
    'boomboomeeraaang' returns 'bombomerang' .
    '''
    new_str = ""
    
    if s == "": 
        return s
    
    for i in range(len(s) - 1):
        if s[i] != s[i+1]: 
            new_str += s[i]
                
    return new_str + s[-1]





        
