"""Test Square"""
import unittest
from unittest import mock
import sys
import io

from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_constructor(self):
        """test constructor"""
        rectangle = Square(10, 5, 7, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 99)

    def test_size_getter(self):
        """test set size"""
        rectangle = Square(10)
        self.assertEqual(rectangle.size, 10)

    def test_size_setter(self):
        """test set size"""
        rectangle = Square(20)
        rectangle.size = 99
        self.assertEqual(rectangle.size, 99)

    def test_size_setter_failed(self):
        """test set size"""
        rectangle = Square(32)
        with self.assertRaises(TypeError) as exc:
            rectangle.size = "size"
            self.assertEqual(str(exc.exception), "width must be an integer")
        with self.assertRaises(ValueError) as exc:
            rectangle.size = 0
            self.assertEqual(str(exc.exception), "width must be > 0")

    def test_calculate_area(self):
        """test calculate area"""
        case1 = Square(3)
        self.assertEqual(case1.area(), 9)
        case2 = Square(2)
        self.assertEqual(case2.area(), 4)
        case3 = Square(8, 0, 0, 12)
        self.assertEqual(case3.area(), 64)

    def test_display(self):
        """Test display with X and Y"""
        # Capture and update stdout
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # Start testing
        case1 = Square(3, 2, 2)
        case1.display()
        result = sys.stdout.getvalue()
        expected_output = ("\n"
                           "\n"
                           "  ###\n"
                           "  ###\n"
                           "  ###\n")
        self.assertEqual(result, expected_output)
        # Reset stdout
        sys.stdout = self.original_stdout

    def test_with_print_statement(self):
        """Test the print by implementing __str__"""
        # Capture and update stdout
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # Test case
        case1 = Square(6, 2, 1, 12)
        print(case1)
        result = sys.stdout.getvalue()
        self.assertEqual(result, "[Square] (12) 2/1 - 6/6\n")
        # Reset stdout
        sys.stdout = self.original_stdout

    def test_square_update(self):
        """Test square"""
        square = Square(1, 1, 1, 1)
        square.update(2, 3, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        """test the method to_dictionary"""
        case1 = Square(3, 1, 4, 9)
        expected_output = {
            'id': 9,
            'size': 3,
            'x': 1,
            'y': 4
        }
        to_dict = case1.to_dictionary()
        self.assertEqual(to_dict, expected_output)
        self.assertIsInstance(to_dict, dict)

    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_save_to_file_square(self, mock_open_file):
        """Test save_to_file with a list of Square instances"""
        case1 = Square(5, 2, 3, 1)
        case2 = Square(8, 4, 6, 2)
        Square.save_to_file([case1, case2])
        mock_open_file.assert_called_once_with('Square.json', 'w')
        mock_open_file().write.assert_called_once_with(
            '[{"id": 1, "size": 5, "x": 2, "y": 3}, '
            '{"id": 2, "size": 8, "x": 4, "y": 6}]'
        )

    def test_create_square(self):
        # Test create method for Square
        dictionary = {'id': 2, 'size': 8, 'x': 4, 'y': 6}
        result = Square.create(**dictionary)
        self.assertIsInstance(result, Square)
        self.assertEqual(result.id, 2)
        self.assertEqual(result.size, 8)
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)


if __name__ == '__main__':
    unittest.main()
