#!/usr/bin/python3
import unittest
import lab8_funcs

class TestCount(unittest.TestCase):

    def test1(self):
        self.assertEqual(lab8_funcs.sum_words(['1', '9', '5', 'one', '7', 'two', '4']), 26)
    def test2(self):
        self.assertEqual(lab8_funcs.sum_words(['-5', '-1', '-2', 'thr33', '11ee', '5ive']), -8)
    def test3(self):
        self.assertEqual(lab8_funcs.sum_words(['three', 'two', 'one']), 0)
    def test4(self):
        self.assertEqual(lab8_funcs.sum_words(['1', '8', 'hello', '3', '5ive', '42']), 54)
    def test5(self):
        self.assertEqual(lab8_funcs.sum_words([]), 0)

    def test_max_pop_1(self):
        self.assertEqual(lab8_funcs.max_pop([('China', 1389618778), ('India', 1311559204), ('US', 331883986)]), 'China')
    def test_max_pop_2(self):
        self.assertEqual(lab8_funcs.max_pop([('China'), ('India', 1311559204), ('US', 331883986)]), None)
    def test_max_pop_3(self):
        self.assertEqual(lab8_funcs.max_pop([('China', 1389618778), ('India', 'lots'), ('US', 331883986)]), None)
    def test_max_pop_4(self):
        self.assertEqual(lab8_funcs.max_pop([('Pakistan', 127318112), ('Indonesia', 141944641), ('Canada', 37590000)]), 'Indonesia')
    def test_max_pop_5(self):
        self.assertEqual(lab8_funcs.max_pop([120, 70, 800]), None)

    def test_product_by_index_1(self):
        self.assertEqual(lab8_funcs.product_by_index([5, 2, 9], [1, 0, 1, 1]), 40)
    def test_product_by_index_2(self):
        self.assertEqual(lab8_funcs.product_by_index([5, 2, 9], [1, 0, 1, 5]), None)
    def test_product_by_index_3(self):
        self.assertEqual(lab8_funcs.product_by_index([10, 3, 4, 5, 2, 9], [0, 1, 2, 3, 4, 5]), 10800)
    def test_product_by_index_4(self):
        self.assertEqual(lab8_funcs.product_by_index([], [1, 0, 1, 1]), None)
    def test_product_by_index_5(self):
        self.assertEqual(lab8_funcs.product_by_index([5, 2, 9], [1, -1]), 18)

    def test_coins_1(self):
        self.assertEqual(lab8_funcs.coins('ppp'), 3)
    def test_coins_2(self):
        self.assertEqual(lab8_funcs.coins('pnqqqnd'), 96)
    def test_coins_3(self):
        self.assertEqual(lab8_funcs.coins(''), 0)
    def test_coins_4(self):
        self.assertRaises(ValueError, lambda: lab8_funcs.coins('$42.33'))
    def test_coins_5(self):  
        self.assertRaises(ValueError, lambda: lab8_funcs.coins('qdnpdr'))

    def test_check_name_1(self):
        self.assertEqual(lab8_funcs.check_name('Alex', 'Ufkes'), 'Ufkes, Alex')
    def test_check_name_2(self):
        self.assertEqual(lab8_funcs.check_name('Jack', 'Sparrow'), 'Sparrow, Jack')
    def test_check_name_3(self):
        self.assertRaises(ValueError, lambda: lab8_funcs.check_name('alex', 'ufkes'))
    def test_check_name_4(self):
        self.assertRaises(ValueError, lambda: lab8_funcs.check_name('Super', 'Mari0'))
    def test_check_name_5(self):
        self.assertRaises(ValueError, lambda: lab8_funcs.check_name('Son1c', 'Hedgehog'))

    def test_get_next_int_1(self):
        li = [1, 2, 3, 4, 5]
        self.assertEqual(lab8_funcs.get_next_int(iter(li)), 1)
    def test_get_next_int_2(self):
        li = ['1', '2', '3', '4', '5']
        self.assertEqual(lab8_funcs.get_next_int(iter(li)), None)
    def test_get_next_int_3(self):
        li = [1, 2, 3]
        it = iter(li)
        self.assertEqual(lab8_funcs.get_next_int(it), 1)
        self.assertEqual(lab8_funcs.get_next_int(it), 2)
        self.assertEqual(lab8_funcs.get_next_int(it), 3)
        self.assertEqual(lab8_funcs.get_next_int(it), None)
    def test_get_next_int_4(self):
        li = [1, '2', 3, '4', 5]
        it = iter(li)
        self.assertEqual(lab8_funcs.get_next_int(it), 1)
        self.assertEqual(lab8_funcs.get_next_int(it), 3)
        self.assertEqual(lab8_funcs.get_next_int(it), 5)
        self.assertEqual(lab8_funcs.get_next_int(it), None)
    def test_get_next_int_5(self):
        li = ['Hello', 'World', 17, 2.0, '3', 4, 5]
        it = iter(li)
        self.assertEqual(lab8_funcs.get_next_int(it), 17)
        self.assertEqual(lab8_funcs.get_next_int(it), 4)
        self.assertEqual(lab8_funcs.get_next_int(it), 5)
        self.assertEqual(lab8_funcs.get_next_int(it), None)

if __name__ == '__main__':
    unittest.main(exit=True) 