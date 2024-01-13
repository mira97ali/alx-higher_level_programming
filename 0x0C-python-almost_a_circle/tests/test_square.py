"""Test Square"""
import unittest
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


if __name__ == '__main__':
    unittest.main()
