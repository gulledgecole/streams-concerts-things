import json


def extract_bands_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
        unique_bands = set()
        for key in data:
            bands = data[key].get("Bands", [])
            print(bands)
            unique_bands.update(bands)
        return unique_bands


unqiue = extract_bands_from_json(
    "../concerts/musicfarm_chas/musicfarm_chas_2023-12-29.json"
)
print(unqiue)
