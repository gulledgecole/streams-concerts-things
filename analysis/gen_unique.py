import csv
import os
import json
from collections import Counter

# Output CSV file
csv_filename = "venues_agg.csv"

# Set to store unique identifier values


# Open CSV file for writing
def get_unqiue_venues():
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header to CSV file
        csv_writer.writerow(["identifier", "maximumAttendeeCapacity"])
        folder_path = "../venues"

        # Iterate over each JSON file
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                file_path = os.path.join(folder_path, file_name)

                with open(file_path, "r") as file:
                    data = json.load(file)

                    # Iterate over each dictionary in the JSON file
                    for entry in data:
                        # Extract values
                        identifier = entry.get("identifier")
                        max_capacity = entry.get("maximumAttendeeCapacity")

                        # Append to CSV
                        csv_writer.writerow([identifier, max_capacity])

                        # Add identifier to set
                        if identifier:
                            unique_identifiers.add(identifier)

    # Print the count of unique identifier values
    unique_identifiers = set()
    print(f"Number of unique identifiers: {len(unique_identifiers)}")


def get_unique_bands(folder_path):
    unique_band_ids = Counter()

    # Iterate over each JSON file in the folder
    # for file_name in os.listdir(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file has a .json extension
            if file.endswith(".json"):
                file_path = os.path.join(root, file)

                if os.path.getsize(file_path) > 0:
                    print(file_path)

                    with open(file_path, "r") as file:
                        data = json.load(file)

                        # Iterate over each entry in the JSON file
                        for entry in data:
                            bands = entry.get("bands", [])
                            for band in bands:
                                identifier = band.get("identifier")
                                if identifier:
                                    unique_band_ids[identifier] += 1

    print(f"Total unique bands: {len(unique_band_ids)}")

    # Print the results
    # for band_id, count in unique_band_ids.items():
    #     print(f"Band ID: {band_id}, Occurrences: {count}")


# for root, dirs, files in os.walk("../concerts"):
#         for file in files:
#             # Check if the file has a .json extension
#             if file.endswith(".json"):
#                 # Build the full path to the JSON file
#                 json_path = os.path.join(root, file)
#                 print(json_path)


get_unique_bands("../concerts")
