#!/usr/bin/python3
import unittest
import lab3_funcs

class TestLab3(unittest.TestCase):

    def test_lettergrade_A(self):
        ''' test_grade_A '''
        self.assertEqual(lab3_funcs.lettergrade(95), 'A')
        self.assertEqual(lab3_funcs.lettergrade(88), 'A')
        self.assertEqual(lab3_funcs.lettergrade(80), 'A')
    def test_lettergrade_B(self):
        ''' test_grade_B '''
        self.assertEqual(lab3_funcs.lettergrade(75), 'B')
        self.assertEqual(lab3_funcs.lettergrade(70), 'B')
        self.assertEqual(lab3_funcs.lettergrade(71), 'B')
    def test_lettergrade_C(self):
        ''' test_grade_C '''
        self.assertEqual(lab3_funcs.lettergrade(60), 'C')
        self.assertEqual(lab3_funcs.lettergrade(65), 'C')
        self.assertEqual(lab3_funcs.lettergrade(69), 'C')
    def test_lettergrade_D(self):
        ''' test_grade_D: '''
        self.assertEqual(lab3_funcs.lettergrade(50), 'D')
        self.assertEqual(lab3_funcs.lettergrade(55), 'D')
        self.assertEqual(lab3_funcs.lettergrade(59), 'D')
    def test_lettergrade_F(self):
        ''' test_grade_F: '''
        self.assertEqual(lab3_funcs.lettergrade(0), 'F')
        self.assertEqual(lab3_funcs.lettergrade(30), 'F')
        self.assertEqual(lab3_funcs.lettergrade(49), 'F')
    def test_lettergrade_invalid(self):
        ''' test_invalid_input: '''
        self.assertIsNone(lab3_funcs.lettergrade(-10))
        self.assertIsNone(lab3_funcs.lettergrade(105))
        self.assertIsNone(lab3_funcs.lettergrade(101))


    def test_three_of_a_kind(self):
        ''' test_three_of_a_kind '''
        self.assertEqual(lab3_funcs.duplicates([1, 1, 1]), 'three-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates((2, 2, 2)), 'three-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates('xxx'), 'three-of-a-kind')
    def test_two_of_a_kind(self):
        ''' test_two_of_a_kind '''
        self.assertEqual(lab3_funcs.duplicates([1, 1, 2]), 'two-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates(('a', 'b', 'b')), 'two-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates('xyx'), 'two-of-a-kind')
    def test_one_of_a_kind(self):
        ''' test_one_of_a_kind '''
        self.assertEqual(lab3_funcs.duplicates([1, 2, 3]), 'one-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates((4, 5, 6)), 'one-of-a-kind')
        self.assertEqual(lab3_funcs.duplicates('xyz'), 'one-of-a-kind')
    def test_duplicates_invalid(self):
        ''' test_invalid_input '''
        self.assertEqual(lab3_funcs.duplicates([]), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates([1, 2]), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates([1, 2, 3, 4]), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates(('a', 'b')), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates(('a', 'b', 'c', 'd')), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates('x'), 'invalid input')
        self.assertEqual(lab3_funcs.duplicates('xyzw'), 'invalid input')


    def test_list_of_integer_inputs(self):
        ''' test_list_of_integer_inputs '''
        self.assertEqual(lab3_funcs.inversions([1, 2, 3]), 0)
        self.assertEqual(lab3_funcs.inversions([2, 1, 3]), 1)
        self.assertEqual(lab3_funcs.inversions([2, 3, 1]), 2)
        self.assertEqual(lab3_funcs.inversions([3, 2, 1]), 3)
    def test_string_inputs(self):
        ''' test_string_inputs '''
        self.assertEqual(lab3_funcs.inversions('act'), 0)
        self.assertEqual(lab3_funcs.inversions('cat'), 1)
        self.assertEqual(lab3_funcs.inversions('tac'), 2)
        self.assertEqual(lab3_funcs.inversions('ton'), 3)
    def test_list_of_string_inputs(self):
        ''' test_list_of_string_inputs '''
        self.assertEqual(lab3_funcs.inversions(['apple', 'banana', 'cherry']), 0)
        self.assertEqual(lab3_funcs.inversions(['apple', 'cherry', 'banana']), 1)
        self.assertEqual(lab3_funcs.inversions(['banana', 'cherry', 'apple']), 2)
        self.assertEqual(lab3_funcs.inversions(['cherry', 'banana', 'apple']), 3)
    def test_inversions_invalid(self):
        ''' test_invalid_inputs '''
        self.assertEqual(lab3_funcs.inversions([]), -1)
        self.assertEqual(lab3_funcs.inversions([1, 2]), -1)
        self.assertEqual(lab3_funcs.inversions([1, 2, 3, 4]), -1)
        self.assertEqual(lab3_funcs.inversions(('a', 'b')), -1)
        self.assertEqual(lab3_funcs.inversions(('a', 'b', 'c', 'd')), -1)
        self.assertEqual(lab3_funcs.inversions('x'), -1)
        self.assertEqual(lab3_funcs.inversions('xyzw'), -1)


    def test_increasing_strict(self):
        ''' test_increasing_strict '''
        self.assertTrue(lab3_funcs.increasing([1, 2, 3], True))
        self.assertFalse(lab3_funcs.increasing([1, 2, 2], True))
        self.assertFalse(lab3_funcs.increasing([3, 2, 1], True))
        self.assertTrue(lab3_funcs.increasing([-1, 0, 1], True))
    def test_increasing_non_strict(self):
        ''' test_increasing_non_strict '''
        self.assertTrue(lab3_funcs.increasing([1, 2, 3], False))
        self.assertTrue(lab3_funcs.increasing([1, 1, 2], False))
        self.assertFalse(lab3_funcs.increasing([3, 2, 1], False))
        self.assertTrue(lab3_funcs.increasing([0, 0, 0], False))
    def test_increasing_invalid(self):
        ''' test_invalid_input '''
        self.assertEqual(lab3_funcs.increasing([], True), 'invalid input')
        self.assertEqual(lab3_funcs.increasing([1, 2], True), 'invalid input')
        self.assertEqual(lab3_funcs.increasing([1, 2, 3, 4], True), 'invalid input')
        self.assertEqual(lab3_funcs.increasing([1, 2, 3], None), 'invalid input')
        self.assertEqual(lab3_funcs.increasing([1, 2, 3], 'string'), 'invalid input')


    def test_addition(self):
        ''' test_addition '''
        self.assertEqual(lab3_funcs.calculator(5, 3, '+'), 8)
        self.assertEqual(lab3_funcs.calculator(-2, 7, '+'), 5)
        self.assertEqual(lab3_funcs.calculator(0, 0, '+'), 0)
    def test_subtraction(self):
        ''' test_subtraction '''
        self.assertEqual(lab3_funcs.calculator(5, 3, '-'), 2)
        self.assertEqual(lab3_funcs.calculator(7, -2, '-'), 9)
        self.assertEqual(lab3_funcs.calculator(0, 0, '-'), 0)
    def test_multiplication(self):
        ''' test_multiplication '''
        self.assertEqual(lab3_funcs.calculator(5, 3, '*'), 15)
        self.assertEqual(lab3_funcs.calculator(-2, -7, '*'), 14)
        self.assertEqual(lab3_funcs.calculator(0, 5, '*'), 0)
    def test_division(self):
        ''' test_division '''
        self.assertEqual(lab3_funcs.calculator(6, 2, '/'), 3)
        self.assertEqual(lab3_funcs.calculator(10, -2, '/'), -5)
        self.assertIsNone(lab3_funcs.calculator(5, 0, '/'))
    def test_exponentiation(self):
        ''' test_exponentiation '''
        self.assertEqual(lab3_funcs.calculator(2, 3, '**'), 8)
        self.assertEqual(lab3_funcs.calculator(5, 0, '**'), 1)
        self.assertEqual(lab3_funcs.calculator(4, -1, '**'), 0.25)
    def test_invalid_operator(self):
        ''' test_invalid_operator '''
        self.assertIsNone(lab3_funcs.calculator(5, 3, 'invalid'))
        self.assertIsNone(lab3_funcs.calculator(2, 4, ''))
        self.assertIsNone(lab3_funcs.calculator(1, 1, None))


if __name__ == '__main__':
    unittest.main(exit=True)