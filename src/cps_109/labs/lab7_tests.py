#!/usr/bin/python3
import unittest
import sys
from bdb import Bdb
import lab7_funcs as lab7

class RecursionDetected(Exception):
    pass

class RecursionDetector(Bdb):
    def do_clear(self, arg):
        pass
    def __init__(self, *args):
        Bdb.__init__(self, *args)
        self.stack = set()
    def user_call(self, frame, argument_list):
        code = frame.f_code
        if code in self.stack:
            raise RecursionDetected
        self.stack.add(code)
    def user_return(self, frame, return_value):
        self.stack.remove(frame.f_code)

def test_recursion(func):
    detector = RecursionDetector()
    detector.set_trace()
    try:
        func()
    except RecursionDetected:
        return True
    else:
        return False
    finally:
        sys.settrace(None)

class TestLab7(unittest.TestCase):

    def test_count_1(self):
        self.assertEqual(lab7.count([], 42), 0)
    def test_count_2(self):
        self.assertEqual(lab7.count([42], 42), 1)
    def test_count_3(self):
        self.assertEqual(lab7.count([1], 42), 0)
    def test_count_4(self):
        self.assertTrue(test_recursion(lambda: lab7.count([1, 2, 3, 2, 4, 2], 2)), "Recursion NOT detected")
        self.assertEqual(lab7.count([1, 2, 3, 2, 4, 2], 2), 3)
    def test_count_5(self):
        self.assertTrue(test_recursion(lambda: lab7.count([1, 2, 3, 4, 5], 6)), "Recursion NOT detected")
        self.assertEqual(lab7.count([1, 2, 3, 4, 5], 6), 0)
    def test_count_6(self):
        self.assertTrue(test_recursion(lambda: lab7.count(["apple", "banana", "apple", "cherry"], "apple")), "Recursion NOT detected")
        self.assertEqual(lab7.count(["apple", "banana", "apple", "cherry"], "apple"), 2)
    def test_count_7(self):
        self.assertTrue(test_recursion(lambda: lab7.count([1, "apple", 2, "banana", 2, "cherry", 2], 2)), "Recursion NOT detected")
        self.assertEqual(lab7.count([1, "apple", 2, "banana", 2, "cherry", 2], 2), 3)
    def test_count_8(self):
        self.assertTrue(test_recursion(lambda: lab7.count([1, None, True, False, None, 1, 42, "apple", None], None)), "Recursion NOT detected")
        self.assertEqual(lab7.count([1, None, True, False, None, 1, 42, "apple", None], None), 3)

    def test_integer_sum_1(self):
        self.assertEqual(lab7.integer_sum([]), 0)
    def test_integer_sum_2(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([1, 2, 3, 4, 5])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([1, 2, 3, 4, 5]), 15)
    def test_integer_sum_3(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([1, 3, 'hello', 5.66])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([1, 3, 'hello', 5.66]), 4)
    def test_integer_sum_4(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum(['', 'hello', 42, 7])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum(['', 'hello', 42, 7]), 49)
    def test_integer_sum_5(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([True, False, 42, 10])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([True, False, 42, 10]), 52)
    def test_integer_sum_6(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([1, -2, 3, -4, 5])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([1, -2, 3, -4, 5]), 3)
    def test_integer_sum_7(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([0, 1, 2, 3])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([0, 1, 2, 3]), 6)
    def test_integer_sum_8(self):
        self.assertTrue(test_recursion(lambda: lab7.integer_sum([1.5, 2.5, 3.5])), "Recursion NOT detected")
        self.assertEqual(lab7.integer_sum([1.5, 2.5, 3.5]), 0)
    
    def test_pow_rec_1(self):
        self.assertEqual(lab7.pow_rec(5, 0), 1)
    def test_pow_rec_2(self):
        self.assertEqual(lab7.pow_rec(0, 5), 0)
    def test_pow_rec_3(self):
        self.assertTrue(test_recursion(lambda: lab7.pow_rec(2, 3)), "Recursion NOT detected")
        self.assertEqual(lab7.pow_rec(2, 3), 8)
    def test_pow_rec_4(self):
        self.assertEqual(lab7.pow_rec(1, 100), 1)
    def test_pow_rec_5(self):
        self.assertTrue(test_recursion(lambda: lab7.pow_rec(2, 10)), "Recursion NOT detected")
        self.assertEqual(lab7.pow_rec(2, 10), 1024)
    def test_pow_rec_6(self):
        self.assertTrue(test_recursion(lambda: lab7.pow_rec(10, 2)), "Recursion NOT detected")
        self.assertEqual(lab7.pow_rec(10, 2), 100)
    def test_pow_rec_7(self):
        self.assertTrue(test_recursion(lambda: lab7.pow_rec(7, 7)), "Recursion NOT detected")
        self.assertEqual(lab7.pow_rec(7, 7), 823543)
    def test_pow_rec_8(self):
        self.assertTrue(test_recursion(lambda: lab7.pow_rec(3, 4)), "Recursion NOT detected")
        self.assertEqual(lab7.pow_rec(3, 4), 81)

    def test_is_palindrome_1(self):
        self.assertTrue(lab7.is_palindrome(''))
    def test_is_palindrome_2(self):
        self.assertTrue(lab7.is_palindrome('a'))
    def test_is_palindrome_3(self):
        self.assertTrue(test_recursion(lambda: lab7.is_palindrome('racecar')), "Recursion NOT detected")
        self.assertTrue(lab7.is_palindrome('racecar'))
    def test_is_palindrome_4(self):
        self.assertFalse(lab7.is_palindrome('mdam'))
    def test_is_palindrome_5(self):
        self.assertTrue(test_recursion(lambda: lab7.is_palindrome('amanaplanacanalpanama')), "Recursion NOT detected")
        self.assertTrue(lab7.is_palindrome('amanaplanacanalpanama'))
    def test_is_palindrome_6(self):
        self.assertFalse(lab7.is_palindrome('hello'))
    def test_is_palindrome_7(self):
        self.assertFalse(lab7.is_palindrome('palindrome'))
    def test_is_palindrome_8(self):
        self.assertTrue(test_recursion(lambda: lab7.is_palindrome('mmmmmmmmmmmmmmammmm')), "Recursion NOT detected")
        self.assertFalse(lab7.is_palindrome('mmmmmmmmmmmmmmammmm'))

    def test_nested_reverse_1(self):
        self.assertEqual(lab7.nested_reverse([]), [])
    def test_nested_reverse_2(self):
        self.assertEqual(lab7.nested_reverse([42]), [42])
    def test_nested_reverse_3(self):
        input_list = [1, 2, [5, 4, 3, [9, 0], 3]]
        expected_output = [[3, [0, 9], 3, 4, 5], 2, 1]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)
    def test_nested_reverse_4(self):
        input_list = [1, [2, [3, []]], []]
        expected_output = [[], [[[], 3], 2], 1]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)
    def test_nested_reverse_5(self):
        input_list = [1, [2, 'abc'], 'def']
        expected_output = ['def', ['abc', 2], 1]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)
    def test_nested_reverse_6(self):
        input_list = [1, [2, 'abc', [3, 4], 5], 6]
        expected_output = [6, [5, [4, 3], 'abc', 2], 1]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)
    def test_nested_reverse_7(self):
        input_list = [1, [2, [2, 2], 2], 1]
        expected_output = [1, [2, [2, 2], 2], 1]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)
    def test_nested_reverse_8(self):
        input_list = [True, [False, [True, False], True], False]
        expected_output = [False, [True, [False, True], False], True]
        self.assertTrue(test_recursion(lambda: lab7.nested_reverse(input_list)), "Recursion NOT detected")
        self.assertEqual(lab7.nested_reverse(input_list), expected_output)

if __name__ == '__main__':
    unittest.main(exit=True)  