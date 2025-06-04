#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, "r", newline='') as f:
            dict_csv = []
            reader = csv.DictReader(f)
            for row in reader:
                dict_csv.append(row)
        with open("data.json", "w") as f:
            json.dump(dict_csv, f)
        return True
    except (FileNotFoundError, csv.Error):
        return False
