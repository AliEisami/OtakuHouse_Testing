import json
from datetime import datetime


class ConfigProvider:
    @staticmethod
    def load_from_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")