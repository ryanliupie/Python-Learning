# --------------------------------------------------------------
# CODING PROBLEMS: 
# --------------------------------------------------------------

'''

This practice final is similar to your midterm and final exam in terms of format.

It is supposed to help you get an idea of areas where you need to practice more.


Fill in the functions below according to their descriptions. Test
your code by running the file "practice_exam_tests.py"

Make sure your code compiles before you finish the test. Syntax errors are bad! 
Do NOT leave syntax errors in your code! This is VERY important.
Always keep a clean copy that compiles even if you are working on something else.


Do not rename your file. 


'''

# 1) 
def to_binary(n):
    '''
    Assume that n is an integer >= 0.
    Return a string representing n in binary (base 2), with no leading zeros.

    For example:
    to_binary(0) returns "0"
    to_binary(1) returns "1"
    to_binary(6) returns "110"
    to_binary(19) returns "10011"

    Hint: Repeatedly divide by 2 and collect remainders.
    '''
    # your code here

# 2) 
def sum_diff_merge(a, b):
    '''
    Assume that a and b are lists of integers of the SAME length.

    Create and return a new sorted list as follows:
      - For each index i, add TWO numbers to the result:
            1) a[i] + b[i]      (the sum at index i)
            2) abs(a[i] - b[i]) (the absolute difference at index i)

    After processing all indices, sort the result in ascending order
    and return it.

    Example:
        a = [5, 2, 9, 1]
        b = [3, 7, 4, 6]

      Index-wise sums and diffs:
        i=0 -> sum=8,  diff=2
        i=1 -> sum=9,  diff=5
        i=2 -> sum=13, diff=5
        i=3 -> sum=7,  diff=5

      Unsorted result: [8, 2, 9, 5, 13, 5, 7, 5]
      Sorted result:   [2, 5, 5, 5, 7, 8, 9, 13]

    So sum_diff_merge([5,2,9,1], [3,7,4,6]) returns:
        [2, 5, 5, 5, 7, 8, 9, 13]

    '''
    # your code here


# 3) 
def count_occurrences(items, target):
    '''
    Assume that items is a (possibly nested) list whose elements are either:
      - integers, or
      - lists with the same kind of structure.

    Return the number of times target appears anywhere inside items.

    You MUST solve this using recursion.

    Examples:
      count_occurrences([1, 2, 3], 2) returns 1

      count_occurrences([1, [2, 3, 2], 4], 2) returns 2

      count_occurrences([[2, 2], [3, [4, 2]]], 2) returns 3

      count_occurrences([], 5) returns 0

    Notes:
    - items can be nested to any depth.
    - You may assume there are no other data types besides int or list.
    '''
    # your code here



# 4)
def row_col_sums(mat):
    '''
    Assume that mat is a non-empty matrix (list of lists) of integers.
    You may assume all rows have the same length.

    Return a tuple of two lists: (row_sums, col_sums) where:
      - row_sums[i] is the sum of the elements in row i
      - col_sums[j] is the sum of the elements in column j

    Example:
        mat = [
            [1, 2, 3],
            [4, 5, 6]
        ]

    row_sums = [1+2+3, 4+5+6] = [6, 15]
    col_sums = [1+4, 2+5, 3+6] = [5, 7, 9]

    So row_col_sums(mat) returns:
        ([6, 15], [5, 7, 9])

    '''
    # your code here



# 5)
def invert_dict(d):
    '''
    Assume that d is a dictionary where:
      - keys are strings
      - values are integers

    Return a NEW dictionary that "inverts" d by grouping keys
    that share the same value.

    The returned dictionary should map each original value
    to a SORTED list of keys that had that value.

    Example:
        d = {"a": 2, "b": 1, "c": 2, "d": 1}

    You should return:
        {1: ["b", "d"], 2: ["a", "c"]}

   
    '''
    # your code here


# 6)
def safe_int_divide(a, b):
    '''
    Compute a divided by b and return the integer quotient.

    Behavior rules:
      1) If either a or b is NOT an int, raise a TypeError.
      2) If b == 0, raise a ValueError.
      3) Otherwise return a // b (integer division).

    Examples:
      safe_int_divide(10, 3) returns 3
      safe_int_divide(-7, 2) returns -4

      safe_int_divide(5, 0) raises ValueError
      safe_int_divide(5.0, 2) raises TypeError
      safe_int_divide("5", 2) raises TypeError

    Notes:
    - You must use explicit type checking.
    - Do not print anything.
    '''
    # your code here

   

