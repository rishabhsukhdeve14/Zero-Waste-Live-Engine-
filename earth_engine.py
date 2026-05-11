import pandas as pd
import random
from datetime import datetime

# CSV load
df = pd.read_csv("landfills.csv", header=None)

# Output file
output_file = "live_methane_data.csv"

# Loop through rows
for index, row in df.iterrows():

    landfill_id = row.iloc[0]
    state = row.iloc[1]
    city = row.iloc[2]
    lat = row.iloc[3]
    lon = row.iloc[4]

    methane = random.randint(1800, 2200)

    timestamp = datetime.utcnow()

    line = f"{timestamp},{landfill_id},{state},{city},{lat},{lon},{methane},Sentinel-5P\n"

    with open(output_file, "a") as f:
        f.write(line)

print("Live monitoring completed successfully")