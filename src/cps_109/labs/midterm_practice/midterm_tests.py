#!/usr/bin/python3
import unittest
import midterm_funcs as mf

class TestMidterm109(unittest.TestCase):

    def test_q1_01(self):
        self.assertEqual(mf.roman_to_arabic('I'), 1)
    def test_q1_02(self):
        self.assertEqual(mf.roman_to_arabic('II'), 2)
    def test_q1_03(self):
        self.assertEqual(mf.roman_to_arabic('III'), 3)
    def test_q1_04(self):
        self.assertEqual(mf.roman_to_arabic('IV'), 4)
    def test_q1_05(self):
        self.assertEqual(mf.roman_to_arabic('V'), 5)
    def test_q1_06(self):
        self.assertEqual(mf.roman_to_arabic('VI'), 6)
    def test_q1_07(self):
        self.assertEqual(mf.roman_to_arabic('VII'), 7)
    def test_q1_08(self):
        self.assertEqual(mf.roman_to_arabic('VIII'), 8)
    def test_q1_09(self):
        self.assertEqual(mf.roman_to_arabic('IX'), 9)
    def test_q1_10(self):
        self.assertEqual(mf.roman_to_arabic('X'), 10)

    def test_q2_01(self):
        self.assertEqual(mf.sum_even(1), 0)
    def test_q2_02(self):
        self.assertEqual(mf.sum_even(2), 2)
    def test_q2_03(self):
        self.assertEqual(mf.sum_even(3), 2)
    def test_q2_04(self):
        self.assertEqual(mf.sum_even(4), 6)
    def test_q2_05(self):
        self.assertEqual(mf.sum_even(5), 6)
    def test_q2_06(self):
        self.assertEqual(mf.sum_even(6), 12)
    def test_q2_07(self):
        self.assertEqual(mf.sum_even(7), 12)
    def test_q2_08(self):
        self.assertEqual(mf.sum_even(8), 20)
    def test_q2_09(self):
        self.assertEqual(mf.sum_even(9), 20)
    def test_q2_10(self):
        self.assertEqual(mf.sum_even(10), 30)

    def test_q3_01(self):
        self.assertEqual(mf.integers_exceed(0), 1)
    def test_q3_02(self):
        self.assertEqual(mf.integers_exceed(1), 2)
    def test_q3_03(self):
        self.assertEqual(mf.integers_exceed(2), 2)
    def test_q3_04(self):
        self.assertEqual(mf.integers_exceed(3), 3)
    def test_q3_05(self):
        self.assertEqual(mf.integers_exceed(4), 3)
    def test_q3_06(self):
        self.assertEqual(mf.integers_exceed(5), 3)
    def test_q3_07(self):
        self.assertEqual(mf.integers_exceed(6), 4)
    def test_q3_08(self):
        self.assertEqual(mf.integers_exceed(7), 4)
    def test_q3_09(self):
        self.assertEqual(mf.integers_exceed(8), 4)
    def test_q3_10(self):
        self.assertEqual(mf.integers_exceed(11), 5)

    def test_q4_01(self):
        self.assertEqual(mf.pyramid_blocks(1, 1), 1)
    def test_q4_02(self):
        self.assertEqual(mf.pyramid_blocks(2, 2), 5)
    def test_q4_03(self):
        self.assertEqual(mf.pyramid_blocks(3, 2), 8)
    def test_q4_04(self):
        self.assertEqual(mf.pyramid_blocks(2, 3), 8)
    def test_q4_05(self):
        self.assertEqual(mf.pyramid_blocks(4, 4), 30)
    def test_q4_06(self):
        self.assertEqual(mf.pyramid_blocks(5, 3), 26)
    def test_q4_07(self):
        self.assertEqual(mf.pyramid_blocks(3, 5), 26)
    def test_q4_08(self):
        self.assertEqual(mf.pyramid_blocks(6, 6), 91)
    def test_q4_09(self):
        self.assertEqual(mf.pyramid_blocks(7, 7), 140)
    def test_q4_10(self):
        self.assertEqual(mf.pyramid_blocks(10, 12), 495)

    def test_q5_01(self):
        self.assertEqual(mf.first_letter(''), '')
    def test_q5_02(self):
        self.assertEqual(mf.first_letter('5'), 'f')
    def test_q5_03(self):
        self.assertEqual(mf.first_letter('5113'), 'foot')
    def test_q5_04(self):
        self.assertEqual(mf.first_letter('0123456789613'), 'zottffssensot')
    def test_q5_05(self):
        self.assertEqual(mf.first_letter('123'), 'ott')
    def test_q5_06(self):
        self.assertEqual(mf.first_letter('567'), 'fss')
    def test_q5_07(self):
        self.assertEqual(mf.first_letter('1234567890'), 'ottffssenz')
    def test_q5_08(self):
        self.assertEqual(mf.first_letter('0123456789'), 'zottffssen')
    def test_q5_09(self):
        self.assertEqual(mf.first_letter('11111'), 'ooooo')
    def test_q5_10(self):
        self.assertEqual(mf.first_letter('13579'), 'otfsn')

    def test_q6_01(self):
        self.assertEqual(mf.deduplicate('abcdef'), 'abcdef')
    def test_q6_02(self):
        self.assertEqual(mf.deduplicate('feeder'), 'feder')
    def test_q6_03(self):
        self.assertEqual(mf.deduplicate('boomboomeeraaang'), 'bombomerang')
    def test_q6_04(self):
        self.assertEqual(mf.deduplicate('aabbccdd'), 'abcd')
    def test_q6_05(self):
        self.assertEqual(mf.deduplicate('aaaaaabbbcccccddeeeeeeeee'), 'abcde')
    def test_q6_06(self):
        self.assertEqual(mf.deduplicate(''), '')
    def test_q6_07(self):
        self.assertEqual(mf.deduplicate('a'), 'a')
    def test_q6_08(self):
        self.assertEqual(mf.deduplicate('#$#@!#$@!'), '#$#@!#$@!')
    def test_q6_09(self):
        self.assertEqual(mf.deduplicate('a  b  c'), 'a b c')
    def test_q6_10(self):
        self.assertEqual(mf.deduplicate('11223344'), '1234')

if __name__ == '__main__':
    unittest.main(exit=True) 

