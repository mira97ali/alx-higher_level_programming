"""Test Rectangle"""
import unittest
import sys
import io

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_constructor(self):
        """test constructor"""
        rectangle = Rectangle(10, 20, 5, 7, 99)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 99)

    def test_width_setter(self):
        """test set width"""
        rectangle = Rectangle(10, 20)
        rectangle.width = 30
        self.assertEqual(rectangle.width, 30)
    
    def test_width_setter_failed(self):
        """test set width"""
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError) as exc:
            rectangle.width = "width"
            self.assertEqual(str(exc.exception), "width must be an integer")
        with self.assertRaises(ValueError) as exc:
            rectangle.width = 0
            self.assertEqual(str(exc.exception), "width must be > 0")

    def test_height_setter(self):
        """test set height"""
        rectangle = Rectangle(10, 20)
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

    def test_height_setter_failed(self):
        """test set height"""
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError) as exc:
            rectangle.height = "height"
            self.assertEqual(str(exc.exception), "height must be an integer")
        with self.assertRaises(ValueError) as exc:
            rectangle.height = 0
            self.assertEqual(str(exc.exception), "height must be > 0")

    def test_x_setter(self):
        """test set x"""
        rectangle = Rectangle(10, 20)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)
    
    def test_x_setter_failed(self):
        """test set x"""
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError) as exc:
            rectangle.x = "x"
            self.assertEqual(str(exc.exception), "x must be an integer")
        with self.assertRaises(ValueError) as exc:
            rectangle.x = -1
            self.assertEqual(str(exc.exception), "x must be >= 0")

    def test_y_setter(self):
        """test set y"""
        rectangle = Rectangle(10, 20)
        rectangle.y = 7
        self.assertEqual(rectangle.y, 7)
    
    def test_y_setter_failed(self):
        """test set y"""
        rectangle = Rectangle(10, 20)
        with self.assertRaises(TypeError) as exc:
            rectangle.y = "y"
            self.assertEqual(str(exc.exception), "y must be an integer")
        with self.assertRaises(ValueError) as exc:
            rectangle.y = -1
            self.assertEqual(str(exc.exception), "y must be >= 0")
    
    def test_calculate_area(self):
        """test calculate area"""
        case1 = Rectangle(3, 2)
        self.assertEqual(case1.area(), 6)
        case2 = Rectangle(2, 10)
        self.assertEqual(case2.area(), 20)
        case3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(case3.area(), 56)

    def test_display_without_x_and_y(self):
        """Test display without X and Y"""
        # Capture and update stdout
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # Start testing
        case1 = Rectangle(4, 6)
        case1.display()
        result = sys.stdout.getvalue()
        expected_output = ("####\n"
                           "####\n"
                           "####\n"
                           "####\n"
                           "####\n"
                           "####\n")
        self.assertEqual(result, expected_output)
        # Reset stdout
        sys.stdout = self.original_stdout

    def test_display_with_x_and_y(self):
        """Test display with X and Y"""
        # Capture and update stdout
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # Start testing
        case1 = Rectangle(2, 3, 2, 2)
        case1.display()
        result = sys.stdout.getvalue()
        expected_output = ("\n"
                           "\n"
                           "  ##\n"
                           "  ##\n"
                           "  ##\n")
        self.assertEqual(result, expected_output)
        # Reset stdout
        sys.stdout = self.original_stdout
    
    def test_with_print_statement(self):
        """Test the print by implementing __str__"""
        # Capture and update stdout
        self.original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        # Test case
        case1 = Rectangle(4, 6, 2, 1, 12)
        print(case1)
        result = sys.stdout.getvalue()
        self.assertEqual(result, "[Rectangle] (12) 2/1 - 4/6\n")
        # Reset stdout
        sys.stdout = self.original_stdout

    def test_update_args_only(self):
        """test the public `update` method, args only"""
        case1 = Rectangle(10, 10, 10, 10)
        case1.update(89)
        self.assertEqual(case1.id, 89)
        # Test width
        self.assertEqual(case1.width, 10)
        case1.update(89, 2)
        self.assertEqual(case1.width, 2)
        # Test height
        self.assertEqual(case1.height, 10)
        case1.update(89, 2, 3)
        self.assertEqual(case1.height, 3)
        # Test x
        self.assertEqual(case1.x, 10)
        case1.update(89, 2, 3, 4)
        self.assertEqual(case1.x, 4)
        # Test y
        self.assertEqual(case1.y, 10)
        case1.update(89, 2, 3, 4, 5)
        self.assertEqual(case1.y, 5)

    def test_update_args_and_kwargs(self):
        """test the public `update` method, args and kwargs"""
        case1 = Rectangle(10, 20, 5, 5)
        case1.update(42, height=30, x=8)
        self.assertEqual(case1.id, 42)
        self.assertEqual(case1.width, 10)
        self.assertEqual(case1.height, 30)
        self.assertEqual(case1.x, 8)
        self.assertEqual(case1.y, 5)

    def test_update_kwargs_only(self):
        """test the public `update` method, args only"""
        case1 = Rectangle(5, 5, 1, 1)
        case1.update(id=0, y=3, width=8)
        self.assertEqual(case1.id, 0)
        self.assertEqual(case1.width, 8)
        self.assertEqual(case1.height, 5)
        self.assertEqual(case1.x, 1)
        self.assertEqual(case1.y, 3)


if __name__ == '__main__':
    unittest.main()
