'''
No description needed at this point. Fill in the functions, you
know the drill. These functions are trickier than the standard
fare from previous labs, and may benefit from clever use of 
data structures (lists, sets, dictionaries) and nested looping.

Each of these problems comes with an additional "challenge mode"
description that will test your ability to produce more efficent
code. Your code should make the CPU work smart, not hard. Solving
the challenge mode is not required to pass the tester.

'''


# --------------------------------------------------------------
# 1) Largest possible difference
# --------------------------------------------------------------

def largest_diff(items):

    '''
    This first question is very simple, and is intended to convey 
    the spirit behind the challenge modes.

    Assume that items is a list of integers. Find and return the 
    largest possible difference between any two values in the list.
    
    AMATEUR HOUR:

    Using a nested loop, calculate the difference between every
    possible pair of values. Return the largest.

    CHALLENGE MODE: 
    
    Avoid nested loops. Avoid writing your own loops entirely
    in favor of using two calls to built-in Python functions.
    This function can be solved with a single line of code.

    '''

    return max(items) - min(items)

# --------------------------------------------------------------
# 2) Target sum of two list elements
# --------------------------------------------------------------

def two_summers(items, target):

    '''
    Assume that items is a sorted list of integers (ascending), 
    and target is an integer value.

    Your goal is to determine if any two elements in items sum
    to the target value. If so, return a pair tuple containing 
    those values. The smaller value should be first, and the 
    larger value should be second. If no such pair sum exists, 
    return None. If there is more than one way to make the sum,
    you should preference the pair whose smaller value is 
    minimum.
    
    For example, If items is [1, 2, 3, 4, 5] and target is 7,
    you should return (2, 5) and not (3, 4)
    
    CHALLENGE MODE: 
    
    Avoid nested loops. This includes calling built-in functions 
    from inside a loop that themselves perform looping behind 
    the scenes. 

    '''

    pass # replace 'pass' with a return statement.


# --------------------------------------------------------------
# 3) Largest on the left
# --------------------------------------------------------------

def count_dominators(items):

    '''
    This is another great problem from Ilkka's problem set.
    
    An element in a list of items is a 'dominator' if every 
    element to its right (not just the one element that is 
    immediately to its right) is strictly smaller than that 
    element. Note how by this definition, the last item of the 
    list is automatically a dominator. 
    
    This function should count how many elements in items are 
    dominators, and return that count.

    For example, the dominators of the list [42, 7, 12, 9, 13, 5] 
    would be the elements 42, 13 and 5.

    CHALLENGE MODE: 

    Avoid nested loops. This includes calling built-in functions 
    from inside a loop that themselves perform looping behind 
    the scenes. 

    '''

    pass # replace 'pass' with a return statement.


# --------------------------------------------------------------
# 4) Rooks on a rampage
# --------------------------------------------------------------

def safe_squares_rooks(n, rooks):

    '''
    This is another great problem from Ilkka's problem set.
    
    A generalized n-by-n chessboard has been invaded by a 
    parliament of rooks, each rook represented as a two-tuple 
    (row, column) of the row and the column of the square that 
    the rook is in. Since we are computer programmers instead of 
    chess players and other healthy and normal folks, our rows 
    and columns are numbered from 0 to n-1. A chess rook covers 
    all squares that are in the same row or in the same column. 

    Given the board size n and the list of rooks on that board, 
    count the number of empty squares that are safe, that is, 
    are not covered by any rook.

    For example: 
    n = 4 and rooks = [(2, 3), (0, 1)] should return 4, since
    four squares are safe from the rooks.

    AMATEUR HOUR:
    
    A catastrophically inefficient way to solve this problem 
    would be to iterate through all n-by-n squares on the 
    board, and then for each of those squares, go through
    every rook in the list to see if that square is safe.

    CHALLENGE MODE: 

    Your mission, should you choose to accept it, is to solve 
    this problem by iterating through the list of rooks once 
    and only once. Clever bookkeeping with auxilliary lists
    or sets might help.

    '''

    pass # replace 'pass' with a return statement.


# --------------------------------------------------------------
# 5) That's enough of you!
# --------------------------------------------------------------

def remove_after_kth(items, k):

    '''
    This is another great problem from Ilkka's problem set.
    
    Given a list of items, some of which may be duplicates, 
    this function should create and return a new list that is 
    otherwise the same as items, but only up to k occurrences 
    of each element are kept, and all occurrences of that 
    element after the first k are discarded.

    AMATEUR HOUR:

    For every element, before adding it to the new list, 
    look back and see if you've already seen k occurrences.

    CHALLENGE MODE:

    Use some clever bookkeeping (pick a good data structure) 
    to avoid ever looking backwards. This includes looking
    backwards in the new list, and the original list. Make
    one pass, and one pass only.

    '''

    pass # replace 'pass' with a return statement.

