import os
import json
import csv


def get_band_venue_count(folder_path):
    """The update method is super cheeky, defined as such:
    The update method of a set in Python is used to add elements from an iterable (such as a list) to the set,
    and it automatically handles duplicates. Sets are dope.
    """
    unique_bands = set()

    # Walk through the directory tree
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file has a .json extension
            if file.endswith(".json"):
                # Build the full path to the JSON file
                json_path = os.path.join(root, file)

                # Read the JSON file
                with open(json_path, "r") as f:
                    data = json.load(f)

                    # Extract bands from the "Bands" key
                    for key in data:
                        bands = data[key].get("Bands", [])
                        unique_bands.update(bands)

    return unique_bands


concerts_folder = "../concerts"
set = get_band_venue_count(concerts_folder)
band_list = list(set)

# Specify the CSV file name
output_csv_file = "unqiue_bands.csv"

# Write the list to the CSV file
with open(output_csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header if needed
    writer.writerow(["Band"])

    # Write the data
    for band in band_list:
        writer.writerow([band])
