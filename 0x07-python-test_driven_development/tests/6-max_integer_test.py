import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Max Integer"""

    def test_empty_list(self):
        """test empty list"""
        result = max_integer()
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """test positive numbers"""
        result = max_integer([1, 5, 3, 9, 2])
        self.assertEqual(result, 9)

    def test_negative_numbers(self):
        """test negative numbers"""
        result = max_integer([-4, -7, -2, -9])
        self.assertEqual(result, -2)

    def test_mixed_numbers(self):
        """test mixed numbers"""
        result = max_integer([1, -5, 3, -9, 2])
        self.assertEqual(result, 3)

    def test_duplicate_numbers(self):
        """test duplicate numbers"""
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_element_list(self):
        """test single element list"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_float_numbers(self):
        """test float numbers"""
        result = max_integer([1.5, 2.7, 3.1, 2.0])
        self.assertEqual(result, 3.1)


if __name__ == '__main__':
    unittest.main()
