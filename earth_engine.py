import pandas as pd
import datetime
import random

timestamp = datetime.datetime.now()

data = {
    "timestamp": [str(timestamp)],
    "methane_ppb": [random.randint(1850, 2100)],
    "latitude": [22.57],
    "longitude": [88.36],
    "satellite": ["Sentinel-5P"]
}

df = pd.DataFrame(data)

df.to_csv(
    "live_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("AUTO DATA UPDATED")
print(data)