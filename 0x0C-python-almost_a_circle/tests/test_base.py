"""Test Base class"""
import unittest
from unittest import mock

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

    def test_to_json_string(self):
        base4 = Base()
        result1 = base4.to_json_string({"a": "a", "b": "b"})
        result2 = base4.to_json_string(None)
        result3 = base4.to_json_string([])
        self.assertEqual(result1, "{\"a\": \"a\", \"b\": \"b\"}")
        self.assertEqual(result2, "[]")
        self.assertEqual(result3, "[]")

    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_save_to_file_empty_list(self, mock_open_file):
        Base.save_to_file([])
        mock_open_file.assert_called_once_with('Base.json', 'w')
        mock_open_file().write.assert_called_once_with('[]')


if __name__ == "__main__":
    unittest.main()
