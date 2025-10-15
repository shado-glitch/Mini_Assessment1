import unittest
import assessment1

class TestAssessment(unittest.TestCase):

    def test_product(self):
        self.assertEqual(12, assessment1.product(3, 4))
        self.assertEqual(121, assessment1.product(11, 11))
        self.assertNotEqual(20, assessment1.product(4, 7))
        self.assertNotEqual(33, assessment1.product(10, 2))

    def test_square(self):
        self.assertEqual(25, assessment1.square(5))
        self.assertEqual(169, assessment1.square(13))
        self.assertNotEqual(27, assessment1.square(4))
        self.assertNotEqual(64, assessment1.square(7))

    def test_even(self):
        self.assertTrue(assessment1.even(4))
        self.assertTrue(assessment1.even(122))
        self.assertFalse(assessment1.even(131))
        self.assertFalse(assessment1.even(11))

    def test_sum_of_list(self):
        self.assertEqual(24, assessment1.sum_of_list([2, 4, 12, 6]))
        self.assertEqual(33, assessment1.sum_of_list([10, 4, 12, 6, 1]))
        self.assertNotEqual(30, assessment1.sum_of_list([22, 4, 12, 6, 3, 7, 1]))
        self.assertNotEqual(24, assessment1.sum_of_list([2, 4, 12, 6, 14, 5, 9]))

    def test_list_even(self):
        self.assertEqual([2,4,6,8,10,12,14,16,18], assessment1.list_of_even_numbers(20))
        self.assertEqual([2,4,6], assessment1.list_of_even_numbers(8))
        self.assertNotEqual([2,4,6,8,10,12,14,16,18,20,22,25], assessment1.list_of_even_numbers(25))
        self.assertNotEqual([2,4,6,8,10,12], assessment1.list_of_even_numbers(10))

    def test_sum_of_odd(self):
        self.assertEqual(49, assessment1.sum_of_odd_numbers([2,5,3,7,11,24,23]))
        self.assertEqual(43, assessment1.sum_of_odd_numbers([3,4,9,22,100,1,6,17,13]))
        self.assertNotEqual(101, assessment1.sum_of_odd_numbers([2,5,3,7,11,24,23]))
        self.assertNotEqual(66, assessment1.sum_of_odd_numbers([3,4,9,22,100,1,6,17,13]))

if __name__ == "__main__":
    unittest.main()