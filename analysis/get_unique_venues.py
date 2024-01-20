import csv
import os
import json

# Output CSV file
csv_filename = "venues_agg.csv"

# Set to store unique identifier values
unique_identifiers = set()


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
    print(f"Number of unique identifiers: {len(unique_identifiers)}")


get_unqiue_venues()
