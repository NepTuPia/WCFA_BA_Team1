import json

def open_json(filename):
    with open(filename, 'r',) as file:
        # JSON 파일을 딕셔너리로 변환
        data_dict = json.load(file)
        return data_dict
def save_dict_from_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def save_dict(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)