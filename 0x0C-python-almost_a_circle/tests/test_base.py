"""Test Base class"""
import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test Base class"""

    def test_same_id(self):
        """test same id"""
        base1 = Base(12)
        base2 = Base(12)
        self.assertNotEqual(base1, base2)
        self.assertEqual(base1.id, base2.id)

    def test_without_ids(self):
        """test none"""
        base3 = Base()
        self.assertEqual(base3.id, 1)


if __name__ == "__main__":
    unittest.main()
