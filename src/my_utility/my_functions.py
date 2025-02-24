import json


# Load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data =  json.load(file)

    for chapter in data:
        chapter["chapter"] = chapter["chapter"].split('/')[0].strip()
    return data
