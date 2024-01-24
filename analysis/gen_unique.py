import csv
import os
import json
import pandas as pd
from collections import Counter


def count_files(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

    return files


# Open CSV file for writing
def get_unqiue_venues():
    with open("venue_list.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header to CSV file
        csv_writer.writerow(["venue_name", "identifier", "maximumAttendeeCapacity"])
        folder_path = "../venues"

        # Iterate over each JSON file
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                file_path = os.path.join(folder_path, file_name)

                with open(file_path, "r") as file:
                    data = json.load(file)
                    for entry in data:
                        # Extract values
                        identifier = entry.get("identifier")
                        max_capacity = entry.get("maximumAttendeeCapacity")
                        venue_name = entry.get("name")
                        csv_writer.writerow([venue_name, identifier, max_capacity])
        df = pd.read_csv("venue_list.csv")
        df_sorted = df.sort_values(by="venue_name", ascending=True)
        df_sorted.to_excel("concerts_list.xlsx", index=False)


def get_unique_bands(folder_path):
    unique_band_ids = Counter()
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
                                name = band.get("name")
                                if name:
                                    unique_band_ids[name] += 1

    print(unique_band_ids)
    print(f"Total unique bands: {len(unique_band_ids)}")
    # with open("band_names_occurances.csv", 'w', newline='') as csvfile:
    #     csv_writer = csv.writer(csvfile)
    #     csv_writer.writerow(["band_name", 'occurrences'])
    #     for name, count in unique_band_ids.items():
    #         csv_writer.writerow([name, count])
    df = pd.DataFrame(
        list(unique_band_ids.items()), columns=["band_name", "occurrences"]
    )

    # Sort the DataFrame by the "occurrences" column in descending order
    df_sorted = df.sort_values(by="occurrences", ascending=False)

    # Specify the Excel file path for export
    excel_file_path = "bands_occurences.xlsx"

    # Export the sorted DataFrame to an Excel sheet
    df_sorted.to_excel(excel_file_path, index=False)

    df = pd.read_csv("band_names_occurances.csv")

    # Sort the DataFrame by the "occurrences" column in descending order
    df_sorted = df.sort_values(by="occurrences", ascending=False)


# get_unique_bands("../concerts")
get_unqiue_venues()
