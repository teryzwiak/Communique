import re

def extract_jinja_statements(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Wzorce dla Jinja
    patterns = {
        "variables": re.compile(r"{{\s*(.*?)\s*}}"),
        "statements": re.compile(r"{%\s*(.*?)\s*%}"),
    }
    
    extracted_data = {
        "variables": patterns["variables"].findall(content),
        "statements": patterns["statements"].findall(content)
    }
    
    return extracted_data
