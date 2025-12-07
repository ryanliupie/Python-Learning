#!/usr/bin/python3
import unittest
import practice_exam as pex



class TestPracticeExam(unittest.TestCase):

# --------------------------------------------------------------
# Q1 TESTS
# --------------------------------------------------------------
    def test_q1_01(self):
        self.assertEqual(pex.to_binary(0), "0")

    def test_q1_02(self):
        self.assertEqual(pex.to_binary(1), "1")

    def test_q1_03(self):
        self.assertEqual(pex.to_binary(2), "10")

    def test_q1_04(self):
        self.assertEqual(pex.to_binary(6), "110")

    def test_q1_05(self):
        self.assertEqual(pex.to_binary(19), "10011")

# --------------------------------------------------------------
# Q2 TESTS
# --------------------------------------------------------------
    def test_q2_01(self):
        self.assertEqual(
        pex.sum_diff_merge([5, 2, 9, 1], [3, 7, 4, 6]),
        [2, 5, 5, 5, 7, 8, 9, 13]
    )

    def test_q2_02(self):
        self.assertEqual(
        pex.sum_diff_merge([10], [4]),
        [6, 14]
    )

    def test_q2_03(self):
        self.assertEqual(
            pex.sum_diff_merge([1, 2, 3], [0, 0, 0]),
            [1, 1, 2, 2, 3, 3]
    )

    def test_q2_04(self):
        self.assertEqual(
        pex.sum_diff_merge([1, 1, 1, 1], [1, 2, 3, 4]),
        [0, 1, 2, 2, 3, 3, 4, 5]
    )

    def test_q2_05(self):
        self.assertEqual(
        pex.sum_diff_merge([-1], [1]),
        [0,2]
    )


# --------------------------------------------------------------
# Q3 TESTS)
# --------------------------------------------------------------
    def test_q3_01(self):
        self.assertEqual(pex.count_occurrences([1, 2, 3], 2), 1)

    def test_q3_02(self):
        self.assertEqual(pex.count_occurrences([1, [2, 3, 2], 4], 2), 2)

    def test_q3_03(self):
        self.assertEqual(pex.count_occurrences([[2, 2], [3, [4, 2]]], 2), 3)

    def test_q3_04(self):
        self.assertEqual(pex.count_occurrences([[], [[], []]], 7), 0)

    def test_q3_05(self):
        self.assertEqual(pex.count_occurrences([5, [5, [5, 5]], 1], 5), 4)


# --------------------------------------------------------------
# Q4 TESTS)
# --------------------------------------------------------------
   
    def test_q4_01(self):
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(pex.row_col_sums(mat), ([6, 15], [5, 7, 9]))
    
    def test_q4_02(self):
        mat = [[7]]
        self.assertEqual(pex.row_col_sums(mat), ([7], [7]))
    
    def test_q4_03(self):
        mat = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(pex.row_col_sums(mat), ([0, 0, 0], [0, 0]))
    
    def test_q4_04(self):
        mat = [[-1, 2], [3, -4]]
        self.assertEqual(pex.row_col_sums(mat), ([1, -1], [2, -2]))
    
    def test_q4_05(self):
        mat = [[1, 2, 3], [10, 20, 30], [-1, -2, -3]]
        self.assertEqual(pex.row_col_sums(mat), ([6, 60, -6], [10, 20, 30]))


# --------------------------------------------------------------
# Q5 TESTS)
# --------------------------------------------------------------

    def test_q5_01(self):
        d = {"a": 2, "b": 1, "c": 2, "d": 1}
        self.assertEqual(pex.invert_dict(d), {1: ["b", "d"], 2: ["a", "c"]})
    
    def test_q5_02(self):
        d = {"x": 5}
        self.assertEqual(pex.invert_dict(d), {5: ["x"]})
    
    def test_q5_03(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(pex.invert_dict(d), {1: ["a"], 2: ["b"], 3: ["c"]})
    
    def test_q5_04(self):
        d = {"cat": 0, "dog": 0, "ant": 0}
        self.assertEqual(pex.invert_dict(d), {0: ["ant", "cat", "dog"]})
    
    def test_q5_05(self):
        d = {"z": -1, "y": -1, "x": 2, "w": 2}
        self.assertEqual(pex.invert_dict(d), {-1: ["y", "z"], 2: ["w", "x"]})


# --------------------------------------------------------------
# Q6 TESTS)
# --------------------------------------------------------------
   
    def test_q6_01(self):
        self.assertEqual(pex.safe_int_divide(10, 3), 3)
    
    def test_q6_02(self):
        self.assertEqual(pex.safe_int_divide(-7, 2), -4)
    
    def test_q6_03(self):
        with self.assertRaises(ValueError):
            pex.safe_int_divide(5, 0)
    
    def test_q6_04(self):
        with self.assertRaises(TypeError):
            pex.safe_int_divide(5.0, 2)
    
    def test_q6_05(self):
        with self.assertRaises(TypeError):
            pex.safe_int_divide("5", 2)


if __name__ == '__main__':
    unittest.main(exit=True) 
