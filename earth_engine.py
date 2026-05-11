import pandas as pd
import datetime
import random

timestamp = datetime.datetime.now()

data = {
    "timestamp": [str(timestamp)],
    "landfill_id": ["IND_001"],
    "state": ["West Bengal"],
    "city": ["Kolkata"],
    "latitude": [22.57],
    "longitude": [88.36],
    "methane_ppb": [random.randint(1850, 2100)],
    "satellite": ["Sentinel-5P"],
    "risk_score": [random.randint(1, 10)]
}

df = pd.DataFrame(data)

df.to_csv(
    "live_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("ADVANCED DATA UPDATED")
print(data)