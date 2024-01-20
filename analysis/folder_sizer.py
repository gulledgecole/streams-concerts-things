import os
import shutil


def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)  # Convert bytes to megabytes


# Replace 'your_folder_path' with the actual path to your folder
folder_path = "/Users/colegulledge/code/thing/streams-concerts-things/venues"

if os.path.exists(folder_path):
    size_in_mb = get_folder_size(folder_path)
    print(f"The size of the folder is approximately {size_in_mb:.2f} MB.")
else:
    print("The specified folder path does not exist.")

get_folder_size(folder_path)
