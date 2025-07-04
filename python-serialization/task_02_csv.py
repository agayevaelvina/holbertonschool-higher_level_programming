#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.

    Parameters:
    - csv_filename (str): The name of the CSV file to convert.

    Returns:
    - bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False
