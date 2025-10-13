#!/usr/bin/python3
import unittest
import lab5_funcs

class TestLab5(unittest.TestCase):

    def test_mixedfraction_1(self):
        self.assertEqual(lab5_funcs.mixedfraction(7, 3), (2, 1, 3))
    def test_mixedfraction_2(self):
        self.assertEqual(lab5_funcs.mixedfraction(4, 5), (0, 4, 5))
    def test_mixedfraction_3(self):
        self.assertEqual(lab5_funcs.mixedfraction(9, 3), (3, 0, 3))
    def test_mixedfraction_4(self):
        self.assertIsNone(lab5_funcs.mixedfraction(5, 0))
    def test_mixedfraction_5(self):
        self.assertEqual(lab5_funcs.mixedfraction(0, 8), (0, 0, 8))

    def test_cyclops_1(self):
        self.assertTrue(lab5_funcs.iscyclops(105))
    def test_cyclops_2(self):
        self.assertTrue(lab5_funcs.iscyclops(12037))
    def test_cyclops_3(self):
        self.assertFalse(lab5_funcs.iscyclops(1001))
    def test_cyclops_4(self):
        self.assertFalse(lab5_funcs.iscyclops(12345))
    def test_cyclops_5(self):
        self.assertFalse(lab5_funcs.iscyclops(10045))
    def test_cyclops_6(self):
        self.assertTrue(lab5_funcs.iscyclops(101))
    def test_cyclops_7(self):
        self.assertTrue(lab5_funcs.iscyclops(0))

    def test_paritypartition_1(self):
        self.assertEqual(lab5_funcs.paritypartition([7, 0, 2, -1, 3, 4, 1]), [0, 2, 4, 7, -1, 3, 1])
    def test_paritypartition_2(self):
        self.assertEqual(lab5_funcs.paritypartition([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])
    def test_paritypartition_3(self):
        self.assertEqual(lab5_funcs.paritypartition([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
    def test_paritypartition_4(self):
        self.assertEqual(lab5_funcs.paritypartition([]), [])
    def test_paritypartition_5(self):
        self.assertEqual(lab5_funcs.paritypartition([-2, 5, -4, 3, -6]), [-2, -4, -6, 5, 3])

    def test_altsignsum_1(self):
        self.assertEqual(lab5_funcs.altsignsum([3, 5, 2, 4, 8, 2]), 2)
    def test_altsignsum_2(self):
        self.assertEqual(lab5_funcs.altsignsum([]), 0)
    def test_altsignsum_3(self):
        self.assertEqual(lab5_funcs.altsignsum([10]), 10)
    def test_altsignsum_4(self):
        self.assertEqual(lab5_funcs.altsignsum([1, 2, 3, 4, 5, 6]), -3)
    def test_altsignsum_5(self):
        self.assertEqual(lab5_funcs.altsignsum([-1, -2, -3, -4, -5, -6]), 3)
    def test_altsignsum_6(self):
        self.assertEqual(lab5_funcs.altsignsum([1, -2, 3, -4, 5, -6]), 21)

    def test_domninocycle_1(self):
        self.assertTrue(lab5_funcs.domninocycle([(3, 5), (5, 2), (2, 3)]))
    def test_domninocycle_2(self):
        self.assertFalse(lab5_funcs.domninocycle([(2, 5), (5, 2), (2, 3)]))
    def test_domninocycle_3(self):
        self.assertTrue(lab5_funcs.domninocycle([]))
    def test_domninocycle_4(self):
        self.assertFalse(lab5_funcs.domninocycle([(2, 5)]))
    def test_domninocycle_5(self):
        self.assertTrue(lab5_funcs.domninocycle([(1, 1)]))
    def test_domninocycle_6(self):
        self.assertTrue(lab5_funcs.domninocycle([(6, 5), (5, 2), (2, 3), (3, 6)]))
    def test_domninocycle_7(self):
        self.assertFalse(lab5_funcs.domninocycle([(3, 5), (5, 1), (2, 3), (3, 3)]))
    def test_domninocycle_8(self):
        self.assertTrue(lab5_funcs.domninocycle([(2, 5), (5, 2), (2, 3), (3, 5), (5, 2)]))
    def test_domninocycle_9(self):
        self.assertFalse(lab5_funcs.domninocycle([(3, 5), (5, 5), (5, 5), (5, 5), (5, 2)]))

if __name__ == '__main__':
    unittest.main(exit=True)