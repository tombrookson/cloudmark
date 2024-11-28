
import unittest
from yaml_utils import process_yaml_content, convert_to_json

class TestYamlUtils(unittest.TestCase):

    def test_process_yaml_content_success(self):
        yaml_content = "key: value"
        result = process_yaml_content(yaml_content)
        self.assertEqual(result, {"key": "value"})

    def test_process_yaml_content_error(self):
        with self.assertRaises(ValueError):
            process_yaml_content("invalid_yaml: [unclosed")

    def test_convert_to_json_success(self):
        yaml_content = {"key": "value"}
        result = convert_to_json(yaml_content)
        self.assertEqual(result, '{\n            "key": "value"\n        }')

    def test_convert_to_json_error(self):
        with self.assertRaises(ValueError):
            convert_to_json(set([1, 2, 3]))

if __name__ == "__main__":
    unittest.main()