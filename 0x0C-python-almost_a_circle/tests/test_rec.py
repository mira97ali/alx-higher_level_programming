"""Test Rectangle"""
import unittest
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

    def test_height_setter(self):
        """test set height"""
        rectangle = Rectangle(10, 20)
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

    def test_x_setter(self):
        """test set x"""
        rectangle = Rectangle(10, 20)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_y_setter(self):
        """test set y"""
        rectangle = Rectangle(10, 20)
        rectangle.y = 7
        self.assertEqual(rectangle.y, 7)


if __name__ == '__main__':
    unittest.main()
