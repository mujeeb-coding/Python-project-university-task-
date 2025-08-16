import csv
import json

# Create a sample CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'score'])
    writer.writeheader()
    writer.writerow({'id': 1, 'name': 'Ali', 'score': 90})
    writer.writerow({'id': 2, 'name': 'Sara', 'score': 85})
    writer.writerow({'id': 3, 'name': 'Ahmed', 'score': 95})

# Convert CSV to JSON
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("CSV converted to JSON successfully.")
