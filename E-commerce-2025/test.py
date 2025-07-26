# converting dataset into json format

import json 
import pandas as pd

df = pd.read_csv('ecommerce_data_2k25.csv')


# Optional: Set an 'id' column if MeiliSearch requires one
df['id'] = df.index + 1  # Auto-generate unique IDs

# Convert to JSON format
json_data = df.to_dict(orient='records')

# Save to a JSON file
import json
with open("dataset.json", "w") as f:
    json.dump(json_data, f, indent=4)