import json


class SecretProvider:
    @staticmethod
    def load_from_file():
        try:
            with open('C:\\Users\\aliei\\Desktop\\5TECH\\OtakuHouse\\automation_testing\\secret.json',
                      'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
