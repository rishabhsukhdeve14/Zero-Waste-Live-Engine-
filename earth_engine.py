import pandas as pd
import datetime
import random

# Read landfill database
landfills = pd.read_csv("landfills.csv")

all_data = []

# Loop through every landfill
for index, row in landfills.iterrows():

    timestamp = datetime.datetime.now()

    methane = random.randint(1850, 2100)

    risk_score = random.randint(1, 10)

    data = {
        "timestamp": str(timestamp),
        "landfill_id": row["landfill_id"],
        "state": row["state"],
        "city": row["city"],
        "latitude": row["latitude"],
        "longitude": row["longitude"],
        "methane_ppb": methane,
        "satellite": "Sentinel-5P",
        "risk_score": risk_score
    }

    all_data.append(data)

# Convert to dataframe
df = pd.DataFrame(all_data)

# Save to CSV
df.to_csv(
    "live_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("MULTI-LANDFILL DATA UPDATED")
print(df)