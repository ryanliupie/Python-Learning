#!/usr/bin/python3
import unittest
import lab4_funcs

class TestLab4(unittest.TestCase):
    
    def test_sum_even_positive_1(self):
        self.assertEqual(lab4_funcs.sumeven(6), 30)  # 2 + 4 + 6 + 8 + 10 = 30
    def test_sum_even_positive_2(self):
        self.assertEqual(lab4_funcs.sumeven(4), 12)  # 0 + 2 + 4 + 6 = 12
    def test_sum_even_zero(self):
        self.assertEqual(lab4_funcs.sumeven(0), 0)  # No even numbers to sum
    def test_sum_even_large(self):
        self.assertEqual(lab4_funcs.sumeven(10**6), 999999000000)  # Sum of first 1 million even numbers


    def test_sum_squares_positive_1(self):
        self.assertEqual(lab4_funcs.sumsquares(5), 55)  # 1 + 4 + 9 + 16 + 25 = 55
    def test_sum_squares_positive_2(self):
        self.assertEqual(lab4_funcs.sumsquares(3), 14)  # 1 + 4 + 9 = 14
    def test_sum_squares_zero(self):
        self.assertEqual(lab4_funcs.sumsquares(0), 0)  # No squares to sum
    def test_sum_squares_large_input(self):
        self.assertEqual(lab4_funcs.sumsquares(10000), 333383335000)  # Sum of squares up to 10000


    def test_odddigitsum_positive_integer(self):
        self.assertEqual(lab4_funcs.odddigitsum(123456789), 25)  # 1 + 3 + 5 + 7 + 9 = 25
    def test_odddigitsum_negative_integer(self):
        self.assertEqual(lab4_funcs.odddigitsum(-13579), 25)  # 1 + 3 + 5 + 7 + 9 = 25
    def test_odddigitsum_positive_integer_with_even_digits(self):
        self.assertEqual(lab4_funcs.odddigitsum(24680), 0)  # No odd digits
    def test_odddigitsum_negative_integer_with_even_digits(self):
        self.assertEqual(lab4_funcs.odddigitsum(-24680), 0)  # No odd digits
    def test_odddigitsum_zero(self):
        self.assertEqual(lab4_funcs.odddigitsum(0), 0)  # No odd digits
    def test_odddigitsum_single_odd_digit(self):
        self.assertEqual(lab4_funcs.odddigitsum(7), 7)  # Single odd digit
    def test_odddigitsum_single_even_digit(self):
        self.assertEqual(lab4_funcs.odddigitsum(4), 0)  # Single even digit
    def test_odddigitsum_large_input(self):
        self.assertEqual(lab4_funcs.odddigitsum(123456789123456789123456789), 75)  # Sum of all odd digits


    def test_listexponential_positive_exponents(self):
        self.assertEqual(lab4_funcs.listexponential(5, 2), [1, 2, 4, 8, 16])
    def test_listexponential_negative_exponent(self):
        self.assertEqual(lab4_funcs.listexponential(3, -2), [1, -2, 4])  # Negative exponent is allowed
    def test_listexponential_float_base(self):
        self.assertEqual(lab4_funcs.listexponential(4, 0.5), [1, 0.5, 0.25, 0.125])
    def test_listexponential_large_exponent(self):
        self.assertEqual(lab4_funcs.listexponential(6, 10), [1, 10, 100, 1000, 10000, 100000])
    def test_listexponential_large_base(self):
        self.assertEqual(lab4_funcs.listexponential(5, 1000), [1, 1000, 1000000, 1000000000, 1000000000000])
    def test_listexponential_mixed_inputs(self):
        self.assertEqual(lab4_funcs.listexponential(4, -0.5), [1, -0.5, 0.25, -0.125])
    def test_listexponential_zero_base(self):
        self.assertEqual(lab4_funcs.listexponential(5, 0), [1, 0, 0, 0, 0])  # Any number to the power of 0 is 1


    def test_digitcat_digits_only(self):
        self.assertEqual(lab4_funcs.digitcat("abc123def456"), 123456)
    def test_digitcat_no_digits(self):
        self.assertIsNone(lab4_funcs.digitcat("abcxyz"))
    def test_digitcat_empty_string(self):
        self.assertIsNone(lab4_funcs.digitcat(""))
    def test_digitcat_digits_with_spaces(self):
        self.assertEqual(lab4_funcs.digitcat("1 2 3 4"), 1234)
    def test_digitcat_digits_with_special_characters(self):
        self.assertEqual(lab4_funcs.digitcat("1$2#3%4"), 1234)
    def test_digitcat_negative_number(self):
        self.assertEqual(lab4_funcs.digitcat("abc-123def"), 123)
    def test_digitcat_decimal_number(self):
        self.assertEqual(lab4_funcs.digitcat("abc3.14def"), 314)
    def test_digitcat_large_number(self):
        self.assertEqual(lab4_funcs.digitcat("abc1234567890def"), 1234567890)
    def test_digitcat_mixed_input(self):
        self.assertEqual(lab4_funcs.digitcat("a1b2c3d4"), 1234)


    def test_stringtofloatlist_positive_integers(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("1.0,2.0,3.0,4.0"), [1.0, 2.0, 3.0, 4.0])
    def test_stringtofloatlist_positive_floats(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("0.1,0.2,0.3,0.4"), [0.1, 0.2, 0.3, 0.4])
    def test_stringtofloatlist_mixed_integers_and_floats(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("1.0,0.5,2.0,1.5"), [1.0, 0.5, 2.0, 1.5])
    def test_stringtofloatlist_negative_numbers(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("-1.0,-2.0,-3.0,-4.0"), [-1.0, -2.0, -3.0, -4.0])
    def test_stringtofloatlist_single_number(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("3.14"), [3.14])
    def test_stringtofloatlist_mixed_input(self):
        self.assertEqual(lab4_funcs.stringtofloatlist("1.0,2.5,-3.0,4.2"), [1.0, 2.5, -3.0, 4.2])


    def test_maxbytype_all_integer(self):
        self.assertEqual(lab4_funcs.maxbytype([3, 1, 4, 2]), (4, None, None))
    def test_maxbytype_all_float(self):
        self.assertEqual(lab4_funcs.maxbytype([3.14, 1.0, 4.2]), (None, 4.2, None))
    def test_maxbytype_all_string(self):
        self.assertEqual(lab4_funcs.maxbytype(['apple', 'banana', 'cherry']), (None, None, 'cherry'))
    def test_maxbytype_mixed_input_small(self):
        self.assertEqual(lab4_funcs.maxbytype([3, 1.5, 'apple', 4.2, 'banana']), (3, 4.2, 'banana'))
    def test_maxbytype_empty_input(self):
        self.assertEqual(lab4_funcs.maxbytype([]), (None, None, None))
    def test_maxbytype_mixed_types_with_none(self):
        self.assertEqual(lab4_funcs.maxbytype([3, 1.5, None, 4.2, 'banana']), (3, 4.2, 'banana'))
    def test_maxbytype_mixed_types_with_none(self):
        mixed_input_with_none = list(range(1000)) + [3.14, 1.0, 4.2] + [None, 'banana', 'cherry']
        self.assertEqual(lab4_funcs.maxbytype(mixed_input_with_none), (999, 4.2, 'cherry'))
    def test_maxbytype_large_input(self):
        large_input = list(range(1000000)) + [None] + ['apple', 'banana', 'cherry']
        self.assertEqual(lab4_funcs.maxbytype(large_input), (999999, None, 'cherry'))


if __name__ == '__main__':
    unittest.main(exit=True)

    