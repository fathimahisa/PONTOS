import requests
import json
from tabulate import tabulate
from config import TOKEN, BASE_URL

PATH = "vessel_data"

# vessel_ids json file
vessel_ids_filename = "vessel_ids.json"

with open(vessel_ids_filename, "r") as json_file:
    vessel_ids_dict = json.load(json_file)

# create a list of tuples for tabulate
table_data = [(key, value) for key, value in vessel_ids_dict.items()]

# print all vessel_ids
print(tabulate(table_data, headers=["Id", "Vessel Name"], tablefmt="fancy_grid"))

vessel_id = input(f"Enter an Id from above table (0 to {len(vessel_ids_dict) - 1}): ")

start_time = input(f"Enter the start time (e.g.: 2024-01-18): ")
end_time = input(f"Enter the end time (e.g.: 2024-01-22): ")

data_limit = input("Enter the data limit: ")

query = (
    "select=time,parameter_id,value::float"  # columns to fetch
    f"&time=gte.{start_time}&time=lt.{end_time}"  # time filter
    f"&vessel_id=eq.{vessel_ids_dict[vessel_id]}"  # vessel_id
    f"&limit={data_limit}"  # data limit
)

# API headers
headers = {"Authorization": f"Bearer {TOKEN}"}

# API call
response = requests.get(f"{BASE_URL}/{PATH}?{query}", headers=headers)
response.raise_for_status()

sensor_data_list = response.json()

# Output file name
output_file = f"{vessel_ids_dict[vessel_id]}_{start_time}_{end_time}.json"

# Save to file
with open(output_file, mode="w") as sensor_json:
    json.dump(sensor_data_list, sensor_json, indent=2)
