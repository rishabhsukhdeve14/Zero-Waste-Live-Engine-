import pandas as pd
import random
from datetime import datetime

# CSV load karo
df = pd.read_csv("landfills.csv")

# Output file
output_file = "live_methane_data.csv"

# Sab rows pe loop
for index, row in df.iterrows():

    landfill_id = row[0]
    state = row[1]
    city = row[2]
    lat = row[3]
    lon = row[4]

    # Dummy methane value
    methane = random.randint(1800, 2200)

    # Timestamp
    timestamp = datetime.utcnow()

    # Save line
    line = f"{timestamp},{landfill_id},{state},{city},{lat},{lon},{methane},Sentinel-5P\n"

    # Append data
    with open(output_file, "a") as f:
        f.write(line)

print("Live monitoring completed")