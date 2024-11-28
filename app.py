import sys
from file_utils import read_file
from yaml_utils import process_yaml_content, convert_to_json

def scan_file(file):
    file_contents = read_file(file)
    file_contents = file_contents.split("\n")
    processed_file = []

    for line in file_contents:
        if "TemplateURL:" in line:
            try:
                url = line.split(": ")[1]
                url_contents = scan_file(url)
                yaml_content = process_yaml_content(url_contents)
                processed_file.append(line.replace(url, "|"))
                processed_file.append("        " + convert_to_json(yaml_content))
            except Exception as e:
                raise ValueError(f"Error processing URL {url}: {e}")
        else:
            processed_file.append(line)
        
    return "\n".join(processed_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        print(scan_file(file_path))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)