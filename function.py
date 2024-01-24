import json


def load_user_data():
    try:
        with open('data.json', 'r+', encoding='utf8') as f:
            return json.load(f)
    except:
        return {}


def save_user_data(user_data):
    with open('data.json', 'w+', encoding='utf8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)
