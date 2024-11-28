
import unittest
from file_utils import read_file
import os

class TestFileUtils(unittest.TestCase):

    def test_read_file_success(self):
        test_file = "test_file.txt"
        with open(test_file, "w") as f:
            f.write("test content")
        content = read_file(test_file)
        self.assertEqual(content, "test content")
        os.remove(test_file)

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file("non_existent_file.txt")

    def test_read_file_error(self):
        with self.assertRaises(IOError):
            read_file("/")

if __name__ == "__main__":
    unittest.main()