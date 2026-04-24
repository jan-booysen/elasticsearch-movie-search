import csv
import json
import re

input_file = "movies.csv"
output_file = "movies.json"

def extract_year(title):
    match = re.search(r"((\d{4}))", title)
    return int(match.group(1)) if match else None

with open(input_file, encoding="utf-8") as csvfile, open(output_file, "w", encoding="utf-8") as jsonfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        movie_id = row["movieId"]
        title = row["title"]
        genres = row["genres"].split("|")
        year = extract_year(title)

        doc = {
            "id": movie_id,
            "title": title.replace(f" ({year})", "") if year else title,
            "year": year,
            "genre": genres
        }

        # Bulk format requires two lines per document
        jsonfile.write(json.dumps({"index": {"_index": "movies", "_id": movie_id}}) + "\n")
        jsonfile.write(json.dumps(doc) + "\n")

    print("Done! movies.json created.")