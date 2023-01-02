import json

# Explore the structure of the data.
filename = 'data/earthquake_1_day_data.json'
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

# Create readable json file
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
   json.dump(all_eq_data, f, indent=4)


