import json


def save_to_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(json.dumps(data))


def load_data(file_path):
    with open(file_path, 'r') as f:
        agents = f.read()
    return json.loads(agents)
