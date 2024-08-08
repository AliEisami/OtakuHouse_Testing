import json
from datetime import datetime


class ConfigProvider:
    @staticmethod
    def load_from_file():
        try:
            with open('C:\\Users\\aliei\\Desktop\\5TECH\\OtakuHouse\\automation_testing\\config.json',
                      'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")

    @staticmethod
    def add_current_time_to_json():
        """
            opens the json file and change the time of the shipDate to the current time
        """
        try:
            with open('C:\\Users\\aliei\\Desktop\\5TECH\\OtakuHouse\\automation_testing\\config.json',
                      'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")

        # Add the current time to a specific item in the JSON data
        data['order']['shipDate'] = datetime.now().isoformat()  # Change 'current_time' to the specific item you want to update

        # Write the updated data back to the JSON file
        try:
            with open('C:\\Users\\aliei\\Desktop\\5TECH\\AutomationFinalProjectPart2\\FinalProjectPart2\\config.json',
                      'w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
