import csv
from pathlib import Path

import requests


API_URL = "http://127.0.0.1:8000/items/"
CSV_FILE = Path(__file__).parent / "MOCK_DATA(1).csv" #path to mock data csv file


def upload_mock_data() -> None:
    with CSV_FILE.open("r", encoding="utf-8", newline="") as file: #opens the csv file and reads through, supports normal text.
        reader = csv.DictReader(file) #reads each row using the column headers as keys.

        for row in reader: #loop for csv file
            item = {
                "name": row["name"].strip(), #.strip removes extra spaces at beginning and end.
                "description": row["description"].strip(),
            }

            response = requests.post(API_URL, json=item, timeout=10) #sends the item to the fastapi enpoint using post.
            response.raise_for_status() #check if backend returned an error

            print(f"Uploaded: {item['name']}")# print to show each successful upload


if __name__ == "__main__": #only runs the upload when directly executed.
    upload_mock_data()