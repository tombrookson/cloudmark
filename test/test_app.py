
import unittest
from app import scan_file
import os

class TestApp(unittest.TestCase):

    def test_scan_file_success(self):
        test_file = "test_file.txt"
        with open(test_file, "w") as f:
            f.write("key: value\nTemplateURL: test_url.txt")
        with open("test_url.txt", "w") as f:
            f.write("url_key: url_value")
        result = scan_file(test_file)
        self.assertIn("key: value", result)
        self.assertIn("TemplateURL: |", result)
        self.assertIn('"url_key": "url_value"', result)
        os.remove(test_file)
        os.remove("test_url.txt")

    def test_scan_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            scan_file("non_existent_file.txt")

    def test_scan_file_error(self):
        test_file = "test_file.txt"
        with open(test_file, "w") as f:
            f.write("TemplateURL: non_existent_url.txt")
        with self.assertRaises(ValueError):
            scan_file(test_file)
        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()