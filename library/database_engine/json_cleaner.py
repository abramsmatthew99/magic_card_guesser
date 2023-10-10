#A file used to clean up the scryfall JSON objects for use with the local database
import settings 
import json

other_cols = ["power", "toughness", "legalities"]

def clean_file(json_file):
    with open(json_file, "r", encoding="utf8") as f:
        data = json.load(f)
        for entry in data:
            clean_data(entry)
    with open(json_file, "w", encoding="utf8") as f:
        json.dump(data,f)

def clean_data(entry: dict):
    for key in list(entry.keys()): 
        if key not in settings.JSON_TO_CARD_COL_NAMES and key not in other_cols:
            entry.pop(key)
        else: 
            if isinstance(entry[key], str):
                entry[key] = entry[key].replace("-", "_")
                entry[key] = entry[key].replace("'", f"\'\'")

if __name__ == "__main__":
    clean_file("assets\JSON Files\oracle-cards-20231009210206.json")
    