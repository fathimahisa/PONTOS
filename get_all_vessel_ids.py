import requests
import json
from config import TOKEN, BASE_URL

PATH = "vessel_ids"

# API headers
headers = {"Authorization": f"Bearer {TOKEN}"}

# API call
response = requests.get(f"{BASE_URL}/{PATH}", headers=headers)
response.raise_for_status()

vessel_ids_list = response.json()

vessel_ids_dict = {i: item["vessel_id"] for i, item in enumerate(vessel_ids_list)}

# Save the data to a JSON file
output_filename = "vessel_ids.json"

with open(output_filename, "w") as json_file:
    json.dump(vessel_ids_dict, json_file, indent=2)

print(f"Vessel ids saved to {output_filename}")
