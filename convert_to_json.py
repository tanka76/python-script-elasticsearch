import csv
import json

csv_file='./data/movies.csv'

json_file='./movies_json.json'


def csv_to_json(csv_file, json_file):
    data=[]
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            genre=row['genres'].split("|")
            data.append({
                "id": row['movieId'],
                "title": row['title'],
                "genres": genre
            })
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)



csv_to_json(csv_file, json_file)

print("Converted Into Json")




