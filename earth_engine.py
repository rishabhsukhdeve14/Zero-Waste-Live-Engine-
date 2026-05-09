import pandas as pd
import datetime
import random

timestamp = datetime.datetime.now()

data = {
    "timestamp": [str(timestamp)],
    "methane_ppb": [random.randint(1700, 2100)],
    "latitude": [22.57],
    "longitude": [88.36]
}

df = pd.DataFrame(data)

df.to_csv("live_methane_data.csv", mode="a", header=False, index=False)

print("Satellite data updated:", timestamp)