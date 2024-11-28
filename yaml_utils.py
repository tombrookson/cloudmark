
import yaml
import json

def process_yaml_content(content):
    try:
        return yaml.load(content, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        raise ValueError(f"Error processing YAML content: {e}")

def convert_to_json(yaml_content):
    try:
        return json.dumps(yaml_content, indent=4).replace("\n", "\n        ")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error converting YAML to JSON: {e}")