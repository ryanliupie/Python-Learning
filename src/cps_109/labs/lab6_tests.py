#!/usr/bin/python3
import unittest
import lab6_funcs

class TestLab6(unittest.TestCase):

    def test_largest_diff_1(self):
        self.assertEqual(lab6_funcs.largest_diff([1, 2, 3, 4, 5]), 4)
    def test_largest_diff_2(self):
        self.assertEqual(lab6_funcs.largest_diff([-5, -3, -1, -4, -2]), 4)
    def test_largest_diff_3(self):
        self.assertEqual(lab6_funcs.largest_diff([-5, 0, 5, -10, 10]), 20)
    def test_largest_diff_4(self):
        self.assertEqual(lab6_funcs.largest_diff([7, 7, 7, 7]), 0)

    def test_two_summers_1(self):
        self.assertEqual(lab6_funcs.two_summers([1, 2, 3, 4, 5], 9), (4, 5))
    def test_two_summers_2(self):
        self.assertIsNone(lab6_funcs.two_summers([1, 2, 3, 4, 5], 10))
    def test_two_summers_3(self):
        self.assertIsNone(lab6_funcs.two_summers([], 10))
    def test_two_summers_4(self):
        self.assertIsNone(lab6_funcs.two_summers([42], 42))
    def test_two_summers_5(self):
        self.assertEqual(lab6_funcs.two_summers([-5, -3, -1, 0, 1, 2, 4], -4), (-5, 1))
    def test_two_summers_6(self):
        self.assertEqual(lab6_funcs.two_summers([1, 2, 2, 3, 4, 4], 5), (1, 4))

    def test_count_dominators_1(self):
        self.assertEqual(lab6_funcs.count_dominators([]), 0)
    def test_count_dominators_2(self):
        self.assertEqual(lab6_funcs.count_dominators([42]), 1)
    def test_count_dominators_3(self):
        self.assertEqual(lab6_funcs.count_dominators([5, 4, 3, 2, 1]), 5)
    def test_count_dominators_4(self):
        self.assertEqual(lab6_funcs.count_dominators([1, 2, 3, 4, 5]), 1) 
    def test_count_dominators_5(self):
        self.assertEqual(lab6_funcs.count_dominators([13, 12, 7, 6, 1, 9, 8, 4]), 5) 
    def test_count_dominators_6(self):
        self.assertEqual(lab6_funcs.count_dominators([42, 7, 12, 9, 13, 5]), 3) 

    def test_safe_squares_rooks_1(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(3, []), 9) 
    def test_safe_squares_rooks_2(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(100, [(r, (r*(r-1))%100) for r in range(0, 100, 2)]), 3900) 
    def test_safe_squares_rooks_3(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(8, [(1, 1), (3, 5), (7, 0), (7, 6)]), 20)
    def test_safe_squares_rooks_4(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(2, [(1, 1)]), 1) 
    def test_safe_squares_rooks_5(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(6, [(r, r) for r in range(6)]), 0) 
    def test_safe_squares_rooks_6(self):
        self.assertEqual(lab6_funcs.safe_squares_rooks(4, [(2, 3), (0, 1)]), 4) 

    def test_remove_after_kth_1(self):
        self.assertEqual(lab6_funcs.remove_after_kth([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2), [1, 2, 2, 3, 3, 4, 4])
    def test_remove_after_kth_2(self):
        self.assertEqual(lab6_funcs.remove_after_kth([1, 2, 3, 4, 5], 2), [1, 2, 3, 4, 5])
    def test_remove_after_kth_3(self):
        self.assertEqual(lab6_funcs.remove_after_kth([], 2), [])
    def test_remove_after_kth_4(self):
        self.assertEqual(lab6_funcs.remove_after_kth([1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5], 3), [1,2,3,4,5,4,3,2,1,2,3,4,5,1,5])
    def test_remove_after_kth_5(self):
        self.assertEqual(lab6_funcs.remove_after_kth(['tom', 42, 'bob', 'bob', 99, 'bob', 'tom', 'tom', 99], 2), ['tom', 42, 'bob', 'bob', 99, 'tom', 99])
    def test_remove_after_kth_6(self):
        self.assertEqual(lab6_funcs.remove_after_kth([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 0), [])

if __name__ == '__main__':
    unittest.main(exit=True)  