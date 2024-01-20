import json
from collections import Counter
import csv

# Extract x-jamBaseMetroId values

with open('us_dump_100k.json', 'r') as file:
    data = json.load(file)

metro_ids = [entry.get('address', {}).get('x-jamBaseMetroId') for entry in data]

# Filter out None values
metro_ids = [id for id in metro_ids if id is not None]

# Count the occurrences of each x-jamBaseMetroId
metro_id_counts = Counter(metro_ids)

# Find unique values and their counts
unique_metro_ids = list(metro_id_counts.keys())
max_count = max(metro_id_counts.values())

# Print the unique values and their counts
print("Unique x-jamBaseMetroId values:", unique_metro_ids)
print("Maximum occurrence count:", max_count)

csv_filename = 'metro_id_counts.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['x-jamBaseMetroId', 'Count'])

    for metro_id, count in metro_id_counts.items():
        csv_writer.writerow([metro_id, count])